def all_left_truncatable_prime(t):
    x = t[93]
    primes = []
    for i in range(2, x):
        if all((int(str(i)[j:]) in primes for j in range(len(str(i))))) and all((int(str(i)[:j]) in primes for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes)