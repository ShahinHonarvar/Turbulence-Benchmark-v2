def find_primes_between_indices(numbers):
    primes = []
    for i in range(69, 85):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort(reverse=True)
    return primes