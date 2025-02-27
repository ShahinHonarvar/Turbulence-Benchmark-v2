def all_left_truncatable_prime(num_tuple):
    x = num_tuple[784]
    left_truncatable_primes = []
    for num in range(2, x):
        left_trunc = str(num)
        while left_trunc and all(map(lambda n: n % i != 0, range(2, int(left_trunc))), int(left_trunc)):
            left_truncatable_primes.append(int(left_trunc))
            left_trunc = left_trunc[1:]
    return sorted(list(set(left_truncatable_primes)))