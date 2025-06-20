from sympy import isprime

def all_left_truncatable_prime(numbers):

    def is_left_truncatable_prime(n):
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:])
        return True
    x = numbers[370]
    return sorted([i for i in range(2, x) if is_left_truncatable_prime(i)], reverse=True)