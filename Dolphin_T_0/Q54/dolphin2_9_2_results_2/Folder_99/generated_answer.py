def all_right_truncatable_prime(tup):
    x = tup[758]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, i))) and all((int(str(i)[:-j]) % len(str(i)[:-j]) != 0 for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)