from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 9:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n < 10 ** 9 else int(str(n)[:-1])
        return True
    return sorted([i for i in range(10, t[74] + 1) if is_left_right_truncatable(i)] if t[74] > 9 else [])