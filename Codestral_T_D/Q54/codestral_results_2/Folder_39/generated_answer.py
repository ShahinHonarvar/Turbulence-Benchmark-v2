def all_right_truncatable_prime(t):
    x = t[30]
    primes = []
    for num in range(x, 1, -1):
        if all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes, reverse=True)