import sympy

def all_left_right_truncatable_prime(n_tuple):

    def is_left_right_truncatable_prime(n, primes):
        num_str = str(n)
        while num_str:
            if int(num_str) not in primes:
                return False
            num_str = num_str[1:-1]
        return True
    pl = list(sympy.primerange(10, n_tuple[89]))
    primes = [p for p in pl if is_left_right_truncatable_prime(p, pl + [10]) and all([i != '0' for i in str(p)])]
    primes.sort(reverse=True)
    return primes