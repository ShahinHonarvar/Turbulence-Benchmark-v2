def find_primes_between_indices(numbers):
    primes = [i for i in numbers[31:68] if all((int(i ** 0.5) + 1 > j or i % j for j in range(2, int(i ** 0.5) + 1))) and i > 1]
    return sorted(primes, reverse=True) if primes else []