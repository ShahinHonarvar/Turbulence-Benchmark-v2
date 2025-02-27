from sympy import isprime

def all_left_truncatable_prime(n):

    def is_left_truncatable_prime(num):
        while num > 0:
            if not isprime(num):
                return False
            num = int(str(num)[1:])
        return True
    primes = [i for i in range(10, n) if is_left_truncatable_prime(i)]
    return sorted(primes)