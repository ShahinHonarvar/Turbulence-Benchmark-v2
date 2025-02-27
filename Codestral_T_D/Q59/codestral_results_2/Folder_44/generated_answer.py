def all_left_truncatable_prime(tup):
    x = tup[39]
    primes = [2]
    for num in range(3, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            left_trunc = [int(str(num)[i:]) for i in range(1, len(str(num)))]
            if all((p in primes for p in left_trunc)):
                primes.append(num)
    return sorted(primes)