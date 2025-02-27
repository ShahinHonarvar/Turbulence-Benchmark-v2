from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[630]

    def is_left_right_trunc_prime(n):
        if not (n >= 10 and isprime(n) and ('0' not in str(n))):
            return False
        while n > 9:
            n = int(str(n)[1:]) if n % 10 != 0 else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_left_right_trunc_prime(i)], reverse=True)