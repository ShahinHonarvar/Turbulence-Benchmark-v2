from sympy import isprime

def all_left_right_truncatable_prime(limit_tuple):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:] if len(str(n)) > 1 else 0)
        return True
    limit = int(isprime(limit_tuple[0]))
    return sorted([x for x in range(2, limit + 1) if is_left_right_truncatable(x)], reverse=True)