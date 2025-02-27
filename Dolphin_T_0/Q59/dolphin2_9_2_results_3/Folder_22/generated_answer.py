def all_left_truncatable_prime(t):
    x = t[85]
    primes = [2, 3, 5, 7]
    for n in range(11, x):
        if all((n % p != 0 for p in primes)):
            primes.append(n)
    result = [i for i in primes if i < x]
    return [i for i in result if all((int(i[j:]) in primes for j in range(1, len(i))))]