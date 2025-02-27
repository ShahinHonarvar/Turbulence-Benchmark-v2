from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 9:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n > 9:
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = tup[81]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable(i)], reverse=True) if x >= 2 else []