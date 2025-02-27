import math

def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    num = numbers[632]
    prime_factors_set = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set