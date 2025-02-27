from sympy import isprime

def all_left_right_truncatable_prime(bound_tuple):

    def is_left_right_truncatable(n):
        while n > 10:
            n = int(str(n)[1:]) if n % 10 != 0 else 0
            if not isprime(n):
                return False
        return True
    x = sorted(set(bound_tuple))[46]
    return sorted([i for i in range(2, x + 1) if isprime(i) and is_left_right_truncatable(i)])[::-1]