from sympy import isprime

def all_left_right_truncatable_prime(xs):

    def is_left_right_truncatable(n):
        while n > 0:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = xs[126]
    left_right_truncatable_primes = []
    for i in range(10, x + 1):
        if isprime(i) and is_left_right_truncatable(i) and (i not in left_right_truncatable_primes):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes