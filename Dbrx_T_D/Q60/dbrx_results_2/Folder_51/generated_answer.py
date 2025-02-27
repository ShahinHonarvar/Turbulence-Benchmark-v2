from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        while num > 10:
            num = int(str(num)[1:])
            if not isprime(num):
                return False
        while num > 0:
            if not isprime(num):
                return False
            num = int(str(num)[:-1])
        return True
    return sorted((x for x in range(1, n + 1) if is_left_right_truncatable_prime(x)))