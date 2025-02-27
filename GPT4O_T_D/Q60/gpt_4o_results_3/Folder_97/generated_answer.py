from sympy import isprime

def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not isprime(int(s))):
                return False
        return True

    def has_no_zero(n):
        return '0' not in str(n)
    x = numbers[645]
    primes = [n for n in range(2, x + 1) if isprime(n) and has_no_zero(n)]
    truncatable_primes = [n for n in primes if is_truncatable_prime(n)]
    return sorted(truncatable_primes)