from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:i + 1])):
                return False
        return True
    x = numbers[175]
    result = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)