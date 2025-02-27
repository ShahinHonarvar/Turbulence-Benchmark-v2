def all_left_truncatable_prime(t):
    primes = [2, 3, 5, 7]
    for i in range(9, t[26], 2):
        if all((i % p > 0 for p in primes)):
            primes.append(i)
            if all((int(i[1:]) in primes for i in str(i)[::-1])):
                pass
    return sorted(primes)