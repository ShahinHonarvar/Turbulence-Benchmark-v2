def all_left_truncatable_prime(t):
    x = t[78]
    primes = [2]
    for num in range(3, x, 2):
        if all((num % p > 0 for p in primes)):
            primes.append(num)
    return [p for p in sorted(primes, reverse=True) if all((int(''.join(str(p)[i:])) in primes for i in range(len(str(p))))) and (not '0' in str(p))]