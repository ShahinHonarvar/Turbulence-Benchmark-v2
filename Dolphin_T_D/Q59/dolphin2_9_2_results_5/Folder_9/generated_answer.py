def all_left_truncatable_prime(t):
    x = t[29]
    primes = [2, 3, 5, 7]
    for possible_prime in range(11, x, 2):
        for i in range(2, possible_prime):
            if possible_prime % i == 0:
                break
        else:
            trunc = possible_prime
            while trunc > 0:
                trunc = trunc // 10
                if trunc != 0 and possible_prime % trunc != 0 and all((trunc % p != 0 for p in primes)):
                    primes.append(possible_prime)
    return sorted(primes, reverse=True)