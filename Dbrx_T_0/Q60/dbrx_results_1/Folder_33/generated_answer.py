from sympy import isprime

def all_left_right_truncatable_prime(n):

    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        while num > 0:
            if not isprime(num):
                return False
            num = int(str(num)[1:]) if num < 10 else int(str(num)[:-1])
        return True
    return sorted([i for i in range(2, n + 1) if is_left_right_truncatable_prime(i)], reverse=True) or []