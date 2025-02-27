from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[10]

    def is_left_right_truncatable(n):
        if str(n)[0] == '0' or not isprime(n) or n <= 10:
            return False
        n = int(str(n)[1:])
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    return sorted([i for i in range(1, x + 1) if is_left_right_truncatable(i)], reverse=True) or [0]