from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = n // 10
        return True
    x = numbers[70]
    return sorted(filter(is_right_truncatable_prime, range(1, x)), reverse=True)