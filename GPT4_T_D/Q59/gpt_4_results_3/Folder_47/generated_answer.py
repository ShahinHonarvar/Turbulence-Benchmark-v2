from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[49]

    def is_left_truncatable_prime(p):
        if '0' in str(p):
            return False
        return all((isprime(int(str(p)[i:])) for i in range(len(str(p)))))
    return sorted((p for p in range(11, x) if isprime(p) and is_left_truncatable_prime(p)))