def all_left_truncatable_prime(t):
    x = t[1]
    primes = [2]
    truncatable_primes = []
    for possible_prime in range(3, x, 2):
        if all((possible_prime % p > 0 for p in primes)):
            primes.append(possible_prime)
            num_str = str(possible_prime)
            if '0' not in num_str and all((int(num_str[i:]) in primes for i in range(1, len(num_str)))):
                truncatable_primes.append(possible_prime)
    return sorted(truncatable_primes, reverse=True)