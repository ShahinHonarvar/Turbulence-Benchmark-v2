def all_left_right_truncatable_prime(t):
    x = t[767]
    primes = []
    for i in range(2, x + 1):
        if all((int(str(i)[j:]) in primes for j in range(1, len(str(i))))) and all((int(str(i)[:j]) in primes for j in range(1, len(str(i))))):
            primes.append(i)
    return sorted(primes, reverse=True)