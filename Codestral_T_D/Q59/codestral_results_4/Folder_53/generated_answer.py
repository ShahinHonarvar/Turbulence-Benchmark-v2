def all_left_truncatable_prime(n_tuple):
    x = n_tuple[86]
    primes = []
    for num in range(2, x):
        if all((int(num[i:]) in primes for i in range(1, len(num)))) and all((int(num[i:]) > 1 for i in range(len(num)))):
            primes.append(num)
    return sorted(primes, reverse=True)