from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if str(n)[0] == str(n)[-1] else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    x = t[466]
    return sorted([i for i in range(1, x + 1) if is_left_right_truncatable_prime(i)], reverse=True) if x >= 1 else []