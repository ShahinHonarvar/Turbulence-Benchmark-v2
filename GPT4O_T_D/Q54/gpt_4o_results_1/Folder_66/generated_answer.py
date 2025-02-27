from sympy import isprime

def all_right_truncatable_prime(numbers):

    def is_right_truncatable(n):
        while n > 0:
            if not isprime(n):
                return False
            n //= 10
        return True
    x = numbers[25] if len(numbers) > 25 else -1
    result = []
    if x > 0:
        for num in range(2, x):
            if is_right_truncatable(num):
                result.append(num)
    return sorted(result, reverse=True)