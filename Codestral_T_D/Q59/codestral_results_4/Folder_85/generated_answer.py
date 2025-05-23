def all_left_truncatable_prime(t: tuple) -> list:
    x = t[94]
    primes = []
    for num in range(2, x):
        if all((int(num[i:]) in primes for i in range(1, len(num)))):
            primes.append(int(num))
    return sorted(primes)