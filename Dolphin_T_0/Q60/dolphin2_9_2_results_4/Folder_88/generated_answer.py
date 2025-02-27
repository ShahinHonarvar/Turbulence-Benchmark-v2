import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def truncate(n):
    while n > 9:
        n = int(str(n)[1:-1])
        if n <= 1:
            return False
    return is_prime(n)

def all_left_right_truncatable_prime(numbers):
    x = numbers[93]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num) and truncate(num):
            primes.append(num)
    return sorted(primes)