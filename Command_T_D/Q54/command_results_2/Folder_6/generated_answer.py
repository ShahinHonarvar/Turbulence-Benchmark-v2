def all_right_truncatable_prime(x):
    x = int(x)
    primes = []
    for i in range(2, x + 1):
        if all((str(i) % j for j in range(2, int(str(i).rstrip('0')) + 1))):
            primes.append(i)
    return sorted(primes)