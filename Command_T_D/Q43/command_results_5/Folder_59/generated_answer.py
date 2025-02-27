def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    maxDivisor = int(num ** 0.5)
    for i in range(5, maxDivisor + 1):
        if num % i == 0:
            return False
    return True