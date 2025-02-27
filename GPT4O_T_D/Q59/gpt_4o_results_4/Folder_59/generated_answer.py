from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while s:
            if not isprime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[84]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes, reverse=True)