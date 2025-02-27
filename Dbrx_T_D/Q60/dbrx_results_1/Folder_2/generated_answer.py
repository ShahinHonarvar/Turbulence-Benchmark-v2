from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 2 else 0
        return True
    x = numbers_tuple[618]
    return sorted(list(filter(is_left_right_truncatable, range(2, x + 1))))