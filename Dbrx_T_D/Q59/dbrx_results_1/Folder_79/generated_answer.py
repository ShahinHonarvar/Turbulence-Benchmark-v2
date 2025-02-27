from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        if n < 10 and isprime(n):
            return True
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    limit = numbers[91]
    return sorted((x for x in range(1, limit) if is_left_truncatable_prime(x)))