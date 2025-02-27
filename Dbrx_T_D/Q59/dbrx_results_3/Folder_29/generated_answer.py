from sympy import isprime

def all_left_truncatable_prime(tup):

    def is_left_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = tup[54]
    primes = [i for i in range(2, x) if is_left_truncatable(i)]
    primes.sort(reverse=True)
    return primes