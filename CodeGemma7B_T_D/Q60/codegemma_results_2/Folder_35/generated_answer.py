from sympy import isprime

def all_left_right_truncatable_prime(x):

    def left_truncate(k):
        if k < 10:
            return None
        while k >= 10:
            k = int(str(k)[:-1])
            if not isprime(k):
                return None
        return k

    def right_truncate(k):
        if k < 10:
            return None
        while k >= 10:
            k = int(str(k)[1:])
            if not isprime(k):
                return None
        return k

    def is_left_right_truncatable_prime(k):
        if '0' in str(k):
            return False
        return left_truncate(k) and right_truncate(k)
    prime_list = [k for k in range(2, x + 1) if isprime(k)]
    return [k for k in prime_list if is_left_right_truncatable_prime(k)]