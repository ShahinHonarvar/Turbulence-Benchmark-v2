from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[65]

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        l = len(s)
        for i in range(l):
            if not isprime(int(s[i:l - i])):
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if isprime(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)