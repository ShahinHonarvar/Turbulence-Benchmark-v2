def all_left_truncatable_prime(t):
    primes = [2]
    x = t[100]
    for i in range(3, x):
        if all((i % p > 0 for p in primes)):
            primes.append(i)
    left_truncatable_prime = []
    for prime in primes:
        if '0' not in str(prime):
            temp = prime
            while temp > 0:
                if not temp in primes:
                    break
                temp, r = divmod(temp, 10)
            else:
                left_truncatable_prime.append(prime)
    return sorted(left_truncatable_prime, reverse=True)