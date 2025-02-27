def all_left_right_truncatable_prime(x_range):
    left_right_truncatable_primes = []
    for prime in range(2, x_range[1] + 1):
        if prime % 2 == 0:
            continue
        if prime % 2 == 1:
            if prime % 10 == 1 or prime % 10 == 5 or prime % 10 == 3:
                if prime % 100 == 1 or prime % 100 == 5 or prime % 100 == 3:
                    left_right_truncatable_primes.append(prime)
    return left_right_truncatable_primes