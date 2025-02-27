def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num):
    if num < 10 and is_prime(num):
        return True
    elif num >= 10 and is_prime(num):
        return left_truncatable_prime(num // 10)
    else:
        return False

def all_left_truncatable_prime(limit):
    primes = []
    for num in range(2, limit):
        if left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)