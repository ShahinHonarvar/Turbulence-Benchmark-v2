from sympy import isprime

def all_right_truncatable_prime(numbers):
    if len(numbers) <= 97:
        return []
    x = numbers[97]

    def is_right_truncatable_prime(n):
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[:-1]
        return True
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes)