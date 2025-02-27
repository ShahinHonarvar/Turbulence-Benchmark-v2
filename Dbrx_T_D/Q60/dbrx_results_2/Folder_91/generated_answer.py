from sympy import isprime

def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 9:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable(i)], reverse=True)