import sympy

def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n < 2:
            return False
        return sympy.isprime(n)

    def is_left_right_truncatable_prime(n):
        if '0' in str(n) or not is_prime(n):
            return False
        while n > 9:
            n //= 10
            if not is_prime(n):
                return False
        return True
    x = numbers_tuple[93]
    return sorted(set(filter(is_left_right_truncatable_prime, range(1, x + 1))))