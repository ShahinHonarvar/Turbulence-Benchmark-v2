from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    limit = numbers[70]
    return sorted([x for x in range(2, limit) if is_left_truncatable_prime(x)], reverse=True)