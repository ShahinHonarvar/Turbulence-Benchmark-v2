def all_left_truncatable_prime(t):
    x = t[7]
    primes = [2, 3, 5, 7]
    for possible_prime in range(11, x):
        if all((possible_prime % p != 0 for p in primes)):
            primes.append(possible_prime)
            if all((int(str(possible_prime)[i:]) != 0 and primes.count(int(str(possible_prime)[i:])) != 0 for i in range(1, len(str(possible_prime))))):
                return sorted(primes)
    return sorted(primes)