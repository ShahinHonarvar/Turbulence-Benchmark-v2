def all_left_truncatable_prime(n):
    x = n[70]
    primes = []
    for i in range(2, x // 2):
        if is_prime(i):
            primes.append(i)
    for p in primes:
        if all((p % d == 0 for d in range(1, int(p ** 0.5) + 1))):
            break
        elif p * 10 ** (len(str(p)) - 1) <= x:
            yield p
    yield from sorted(primes)