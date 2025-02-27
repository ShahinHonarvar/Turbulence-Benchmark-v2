from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not isprime(int(s))):
                return False
        return True
    x = numbers[67]
    primes = [n for n in range(2, x + 1) if isprime(n) and '0' not in str(n)]
    truncatable_primes = [p for p in primes if is_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)