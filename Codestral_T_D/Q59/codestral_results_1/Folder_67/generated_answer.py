def all_left_truncatable_prime(t):
    x = t[71]
    primes = [2]
    for i in range(3, x, 2):
        if all((i % p != 0 for p in primes)) and all((int(str(i)[j:]) in primes for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)