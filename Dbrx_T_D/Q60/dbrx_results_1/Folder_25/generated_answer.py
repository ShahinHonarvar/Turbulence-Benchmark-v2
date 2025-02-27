from sympy import isprime

def all_left_right_truncatable_prime(n: int) -> list[int]:

    def is_left_right_truncatable_prime(i: int) -> bool:
        if not isprime(i) or '0' in str(i):
            return False
        while i > 9:
            i = int(str(i)[1:])
            if not isprime(i):
                return False
        return True
    return sorted((i for i in range(10, n + 1) if is_left_right_truncatable_prime(i)))