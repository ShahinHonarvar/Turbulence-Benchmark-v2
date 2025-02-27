def all_left_truncatable_prime(numbers):
    x = numbers[61]
    primes = []
    for possible_prime in range(2, x):
        if all((possible_prime % i != 0 for i in range(2, possible_prime))):
            truncated = possible_prime
            while truncated:
                if truncated == possible_prime:
                    left_trunc = possible_prime
                else:
                    left_trunc = int(str(possible_prime)[-len(str(truncated)):] + str(left_trunc))
                if all((left_trunc % i != 0 for i in range(2, left_trunc))):
                    truncated = truncated // 10
                else:
                    break
            else:
                primes.append(possible_prime)
    return sorted(primes)