from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if str(n)[0] == '1' else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = tup[767]
    return sorted(filter(is_left_right_truncatable_prime, range(2, x + 1)), reverse=True) if x >= 2 else []