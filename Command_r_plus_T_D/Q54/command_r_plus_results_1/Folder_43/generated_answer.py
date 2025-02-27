def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatable_primes(limit):
    primes = []
    for num in range(limit, 0, -1):
        truncated = True
        temp = num
        while temp > 0:
            temp //= 10
            if not is_prime(num - temp):
                truncated = False
                break
        if truncated and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)

def all_right_truncatable_prime(tup):
    limit = tup[89]
    return right_truncatable_primes(limit)