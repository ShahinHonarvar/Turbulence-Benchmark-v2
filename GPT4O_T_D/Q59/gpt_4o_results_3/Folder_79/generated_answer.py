from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[91]

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        while n:
            if not isprime(n):
                return False
            n //= 10
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])