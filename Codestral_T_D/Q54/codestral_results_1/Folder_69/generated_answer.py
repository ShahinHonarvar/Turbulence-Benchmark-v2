def all_right_truncatable_prime(num_tuple):
    x = num_tuple[760]
    primes = []
    for possible_prime in range(2, x):
        if all((possible_prime % d != 0 for d in range(2, int(possible_prime ** 0.5) + 1))):
            num_str = str(possible_prime)
            if all((int(num_str[:i]) in primes for i in range(1, len(num_str)))):
                primes.append(possible_prime)
    return sorted(primes, reverse=True)