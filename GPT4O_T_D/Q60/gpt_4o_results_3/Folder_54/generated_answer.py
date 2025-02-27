from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_left_right_truncatable_prime(p):
        s = str(p)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:-i])):
                return False
        return True
    x = numbers[88]
    result = []
    for num in range(10, x + 1):
        if isprime(num) and is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)