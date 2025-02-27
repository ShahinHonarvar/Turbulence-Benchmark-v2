from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:])
            if not isprime(n):
                return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[:-1])
        return True
    x = numbers_tuple[429]
    return sorted([num for num in range(2, x + 1) if is_left_right_truncatable(num)], reverse=True) if 10 <= x <= 10 ** 7 else []