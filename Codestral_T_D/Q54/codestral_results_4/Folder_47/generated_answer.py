def all_right_truncatable_prime(numbers):
    x = numbers[49]
    primes = []
    for possible_prime in range(2, x):
        if all((possible_prime % d for d in range(2, int(possible_prime ** 0.5) + 1))) and all((all_right_truncatable_prime(numbers[:49] + (possible_prime // 10,)) for possible_prime in [int(str(possible_prime)[:i]) for i in range(1, len(str(possible_prime)))])):
            primes.append(possible_prime)
    return sorted(primes)