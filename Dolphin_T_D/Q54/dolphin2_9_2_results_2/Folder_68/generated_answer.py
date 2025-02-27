def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_right_truncatable_prime(t):
    x = t[1]
    primes = []
    for i in range(x, 0, -1):
        if is_prime(i):
            j = i
            while j > 1:
                if j % 10 == 0 or not is_prime(j // 10):
                    break
                j //= 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)