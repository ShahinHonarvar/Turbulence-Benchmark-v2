def all_left_truncatable_prime(tup):
    x = tup[370]
    primes = [p for p in range(2, x) if all((int(str(p)[:i]) in [2, 3, 5, 7] for i in range(1, len(str(p))) if int(str(p)[:i]) < 10 or int(str(p)[:i]) % 2 != 0))]
    primes.sort(reverse=True)
    return primes