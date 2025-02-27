import math

def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    number = numbers[19]
    prime_set = set()
    for i in range(2, number + 1):
        if is_prime(i) and number % i == 0:
            prime_set.add(i)
    return prime_set