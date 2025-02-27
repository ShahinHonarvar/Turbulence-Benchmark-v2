from sympy import isprime

def all_left_right_truncatable_prime(upper_bound: tuple) -> list:

    def is_left_right_truncatable_prime(n: int) -> bool:
        if not isprime(n) or '0' in str(n):
            return False
        while n > 1:
            n = int(str(n)[1:]) if len(str(n)) > 1 else 1
            if not isprime(n):
                return False
            n = int(str(n)[:-1]) if len(str(n)) > 1 else 1
        return True
    upper_bound = upper_bound[22]
    return sorted(filter(is_left_right_truncatable_prime, range(1, upper_bound + 1)))