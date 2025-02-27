def find_primes_between_indices(numbers):
    primes = sorted(set((i for i in numbers[30:44] if i > 1 and all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))))))
    return primes