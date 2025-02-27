def all_left_truncatable_prime(r):
    x = r[429]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    left_truncatable_primes = []
    for p in primes:
        if p % 10 == 0:
            continue
        for i in range(1, len(str(p))):
            if not is_prime(int(str(p)[:i])):
                break
        else:
            left_truncatable_primes.append(p)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes