def all_left_truncatable_prime(num_tuple):
    x = num_tuple[370]
    primes = [i for i in range(2, x) if all((int(str(i)[j:]) in [2, 3, 5, 7] for j in range(len(str(i)) - 1, -1, -1)))]
    return sorted(primes, reverse=True)