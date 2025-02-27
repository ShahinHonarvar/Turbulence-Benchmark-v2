from sympy import isprime

def all_left_right_truncatable_prime(upper_bound: tuple) -> list:

    def is_left_right_truncatable_prime(n: int) -> bool:
        if not isprime(n) or '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = upper_bound[645]
    return sorted(filter(is_left_right_truncatable_prime, range(2, x + 1)))