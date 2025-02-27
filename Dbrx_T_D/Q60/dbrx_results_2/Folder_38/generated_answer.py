from sympy import isprime

def all_left_right_truncatable_prime(t):

    def is_left_and_right_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 10:
            n = int(str(n)[1:] if str(n)[0] == '1' else str(n)[:-1])
            if not isprime(n):
                return False
        return True
    return sorted(filter(is_left_and_right_truncatable_prime, range(11, t[28] + 1)))