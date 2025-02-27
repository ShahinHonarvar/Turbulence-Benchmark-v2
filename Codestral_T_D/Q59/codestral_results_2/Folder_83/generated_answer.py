def all_left_truncatable_prime(t):
    x = t[24]
    primes = []
    for num in range(2, x):
        if all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)