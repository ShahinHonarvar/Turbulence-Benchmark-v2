from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):

    def is_left_truncatable_prime(n):
        if n < 10 and isprime(n):
            return True
        while n > 0:
            if not isprime(n):
                return False
            n = n % 10
        return True
    x = numbers_tuple[78]
    return sorted([num for num in range(2, x) if is_left_truncatable_prime(num)], reverse=True)