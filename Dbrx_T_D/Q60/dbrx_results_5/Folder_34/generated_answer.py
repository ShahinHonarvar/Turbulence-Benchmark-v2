from itertools import islice
from sympy import isprime

def all_left_right_truncatable_prime(tuples):

    def left_right_truncatable(prime):
        while prime > 0:
            if not isprime(prime):
                return False
            prime = prime // 10
        return True
    x, = tuples[18]
    result = [i for i in range(1, x + 1) if isprime(i) and left_right_truncatable(i)]
    result.sort(reverse=True)
    return result