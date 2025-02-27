def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqr = int(num ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if num % divisor == 0:
            return False
    return True

def prime_factors(numbers):
    prime_factors_set = set()
    num = numbers[74]
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set