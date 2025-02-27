def find_primes_between_indices(numbers):
    primes = []
    for prime in range(numbers[19], numbers[71] + 1):
        if prime > 1:
            is_prime = True
            for i in range(2, int(prime ** 0.5) + 1):
                if prime % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(prime)
    return sorted(primes)