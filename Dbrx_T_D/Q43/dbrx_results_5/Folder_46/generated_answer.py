def find_primes_between_indices(numbers):
    primes = sorted([i for i in numbers[20:26] if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))], reverse=True)
    return primes