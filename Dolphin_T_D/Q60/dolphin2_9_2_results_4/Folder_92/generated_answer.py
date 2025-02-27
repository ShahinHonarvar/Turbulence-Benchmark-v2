def all_left_right_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    while primes[-1] <= x:
        n = primes[-1]
        if n >= 10 and all((int(n[i:j]) in primes for i in range(1, len(str(n))) for j in range(i + 1, len(str(n)) + 1))):
            primes.append(n * 10 + 3)
    primes.sort()
    return [n for n in primes if n <= x]