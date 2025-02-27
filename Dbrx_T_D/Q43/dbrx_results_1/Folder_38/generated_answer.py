def find_primes_between_indices(numbers):
    prime_numbers = sorted(set((num for num in set(numbers[55:88]) if num > 1 and all((num % i for i in range(2, num))))))
    if not prime_numbers:
        return []
    return prime_numbers