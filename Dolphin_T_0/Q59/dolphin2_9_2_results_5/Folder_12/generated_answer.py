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

def all_left_truncatable_prime(t):
    x = t[70]
    primes = []
    for n in range(x, 0, -1):
        power = len(str(n))
        while power > 0:
            temp = int(n / 10 ** (power - 1))
            if not is_prime(temp):
                break
            power -= 1
        if power == 0:
            primes.append(n)
    return sorted(primes, reverse=True)