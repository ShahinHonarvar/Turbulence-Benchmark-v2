import sympy

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 14:
        return []
    x = numbers[14]
    right_truncatable_primes = []

    def is_right_truncatable_prime(n):
        s = str(n)
        while s:
            if not sympy.isprime(int(s)):
                return False
            s = s[:-1]
        return True
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return right_truncatable_primes