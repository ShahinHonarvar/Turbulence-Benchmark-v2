from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if not isprime(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = numbers[89]
    result = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)