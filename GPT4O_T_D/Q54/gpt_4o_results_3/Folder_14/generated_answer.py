from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[78]

    def is_right_truncatable_prime(n):
        s = str(n)
        while s:
            if not isprime(int(s)):
                return False
            s = s[:-1]
        return True
    primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(primes, reverse=True)