from sympy import isprime

def all_left_right_truncatable_prime(upper_bound_tuple):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    upper_bound = upper_bound_tuple[803]
    primes = [i for i in range(2, upper_bound + 1) if isprime(i) and is_left_right_truncatable_prime(i)]
    return sorted(primes)