def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(x):
    primes = []
    for i in range(10, x):
        if is_prime(i) and '0' not in str(i):
            trunc = i
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)