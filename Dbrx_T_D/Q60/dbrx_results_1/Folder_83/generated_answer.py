from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 9:
            n = int(str(n)[1:]) if n < 100 else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    return sorted([num for num in range(2, numbers_tuple[24] + 1) if is_left_right_truncatable_prime(num)])