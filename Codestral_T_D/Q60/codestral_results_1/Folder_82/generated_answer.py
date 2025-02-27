def all_left_right_truncatable_prime(tup):
    x = tup[69]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))) and all((int(str(num)[i:]) in primes for i in range(1, len(str(num))))) and ('0' not in str(num)):
            primes.append(num)
    return sorted(primes, reverse=True)