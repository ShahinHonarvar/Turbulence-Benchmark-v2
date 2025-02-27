from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True
    x = numbers[7]
    primes = [n for n in range(2, x) if is_left_truncatable(n)]
    return sorted(primes)