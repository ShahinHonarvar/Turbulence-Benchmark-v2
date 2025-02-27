def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[36]
    primes = [2, 3, 5, 7]
    for n in range(10, x):
        if n % 10 in (0, 2, 4, 5, 6, 8) or not is_prime(n):
            continue
        i = n
        while i:
            if not is_prime(i):
                break
            i = i // 10
        else:
            primes.append(n)
    return primes