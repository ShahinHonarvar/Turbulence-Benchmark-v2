from math import isqrt

def right_truncatable_prime(x):
    primes = []
    for num in range(x - 1, 1, -1):
        if all((num % i != 0 for i in range(2, isqrt(num) + 1))):
            trunc = num
            while trunc > 1:
                trunc //= 10
                if not all((trunc % i != 0 for i in range(2, isqrt(trunc) + 1))):
                    break
            else:
                primes.append(num)
    return primes

def all_right_truncatable_prime(numbers):
    if numbers:
        x = numbers[31]
        return right_truncatable_prime(x)
    else:
        return []