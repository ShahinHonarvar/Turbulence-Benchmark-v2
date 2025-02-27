from sympy import isprime

def all_left_right_truncatable_prime(tup):

    def is_left_right_truncatable_prime(n):
        while n > 9 and isprime(n):
            n = int(str(n)[1:]) if n % 10 != 0 else 0
            n = int(str(n)[:-1]) if n > 9 else 0
        return n == 0
    x = tup[7]
    return sorted(filter(is_left_right_truncatable_prime, range(2, x + 1)))