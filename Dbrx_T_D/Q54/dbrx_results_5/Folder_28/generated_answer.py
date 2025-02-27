from sympy import isprime

def all_right_truncatable_prime(x_tuple):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    x = x_tuple[19]
    rt_primes = [i for i in range(1, x) if is_right_truncatable_prime(i)]
    sorted_rt_primes = sorted(rt_primes)
    return sorted_rt_primes