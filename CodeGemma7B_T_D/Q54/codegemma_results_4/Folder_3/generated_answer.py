def all_right_truncatable_prime(tup):
    x = tup[100]
    primes = []
    for i in range(2, x):
        for j in range(i, x):
            if j % i == 0:
                break
        else:
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        for j in range(1, len(str_prime)):
            if int(str_prime[:-j]) not in primes:
                break
        else:
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)