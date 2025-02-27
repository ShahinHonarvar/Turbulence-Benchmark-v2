from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 10:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n > 9:
            n = int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = tup[31]
    return sorted([i for i in range(101, x + 1) if is_left_right_truncatable(i)], reverse=True)