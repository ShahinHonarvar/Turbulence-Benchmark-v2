from sympy import isprime

def all_right_truncatable_prime(x):

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    primes = []
    for num in range(1, x):
        if is_right_truncatable(num):
            primes.append(num)
    return sorted(primes)