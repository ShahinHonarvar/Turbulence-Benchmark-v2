from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable_prime(n):
        if not isprime(n) or '0' in str(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if str(n)[0] == '1' else int(str(n)[1:])
            if not isprime(n):
                return False
        return True
    x = numbers_tuple[46]
    return sorted([i for i in range(1, x + 1) if is_left_right_truncatable_prime(i)], reverse=True)