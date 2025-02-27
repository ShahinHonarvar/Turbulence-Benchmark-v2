import sympy

def all_left_truncatable_prime(numbers):

    def is_prime(n):
        return sympy.isprime(n)

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[33]
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return result