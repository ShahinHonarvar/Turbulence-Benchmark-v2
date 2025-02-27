def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if str(num).count('0') > 0:
        return False
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(limit):
    primes = []
    for num in range(2, limit):
        if left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)