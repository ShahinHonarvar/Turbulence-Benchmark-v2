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
    for i in range(1, len(str(num))):
        if not is_prime(int(str(num)[:i])):
            return False
    return True

def all_left_truncatable_prime(limit):
    primes = []
    for i in range(2, limit[64]):
        if left_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)