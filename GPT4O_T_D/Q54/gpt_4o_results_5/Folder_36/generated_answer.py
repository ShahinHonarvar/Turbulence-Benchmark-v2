from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    if len(numbers) <= 992:
        return []
    x = numbers[992]
    return sorted([n for n in range(2, x) if is_right_truncatable(n)])