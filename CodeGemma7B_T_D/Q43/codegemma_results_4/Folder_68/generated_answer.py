def find_primes_between_indices(numbers):
    primes = [num for num in numbers[1:6] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))]
    return primes if primes else []