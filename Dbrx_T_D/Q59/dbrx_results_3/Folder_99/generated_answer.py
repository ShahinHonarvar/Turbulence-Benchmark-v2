from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    x = numbers_tuple[758]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)])