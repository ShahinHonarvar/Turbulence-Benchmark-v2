from sympy import isprime

def all_left_right_truncatable_prime(int_tuple):

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if str(n)[0] == str(n)[-1] else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = int_tuple[36]
    return sorted((n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)))