def all_left_truncatable_prime(t):
    x = t[20]
    primes = [2]
    i = 3
    while i < x:
        if all((i % p != 0 for p in primes)):
            primes.append(i)
        i += 2
    left_truncatable = []
    for prime in primes:
        temp = prime
        while temp > 1:
            if temp != prime and temp in primes:
                left_truncatable.append(prime)
                break
            temp = int(str(temp)[1:])
    return sorted(left_truncatable, reverse=True)