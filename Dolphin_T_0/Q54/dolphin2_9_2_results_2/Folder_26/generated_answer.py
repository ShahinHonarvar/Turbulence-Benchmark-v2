def all_right_truncatable_prime(num_tuple):
    x = num_tuple[81]
    primes = [2]
    for possible_prime in range(3, x, 2):
        for i in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % i == 0:
                break
        else:
            if str(possible_prime) in [str(x)[-i:] for i in range(1, len(str(x)) + 1) if all((int(str(possible_prime)[-i:]) % p != 0 for p in range(2, int(int(str(possible_prime)[-i:]) ** 0.5) + 1)))]:
                primes.append(possible_prime)
    return sorted(primes, reverse=True) if len(primes) > 1 else []