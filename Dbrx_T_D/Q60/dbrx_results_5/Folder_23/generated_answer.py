from sympy import isprime

def all_left_right_truncatable_prime(r: tuple) -> list:

    def is_left_right_truncatable(n: int) -> bool:
        while n > 0 and n < x:
            if not isprime(n):
                return False
            n = n % 10 // 10 if n < 10 else n % 10
        return True
    x = r[77] if len(r) > 77 else 0
    LRTP = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(LRTP, reverse=True) if LRTP else []