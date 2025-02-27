from sympy import isprime

def all_left_right_truncatable_prime(numbers_tuple):

    def is_left_right_truncatable(n):
        while n > 9:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if n % 10 != 0 else 0
            n = n // 10 if n > 9 else n
        return True
    x = numbers_tuple[35]
    return sorted([i for i in range(2, x + 1) if isprime(i) and is_left_right_truncatable(i)], reverse=True) or []