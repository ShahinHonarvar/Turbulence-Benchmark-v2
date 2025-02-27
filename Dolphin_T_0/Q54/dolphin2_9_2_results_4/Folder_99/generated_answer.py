def all_right_truncatable_prime(arg_tuple):
    x = arg_tuple[758]
    primes = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    right_truncatable_primes = []
    for prime in primes:
        if all((int(str(prime)[j:]) in primes for j in range(1, len(str(prime))))):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)