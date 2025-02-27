from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = numbers_tuple[758]
    return sorted(filter(is_left_truncatable_prime, range(1, x)))