def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[835]
    primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        n = i
        while n > 1:
            if not is_prime(n):
                break
            n //= 10
        else:
            primes.append(i)
    primes.sort()
    return primes