def find_primes_between_indices(numbers):
    primes = [num for num in numbers[32:36] if all((num % i != 0 for i in range(2, num)))]
    return sorted(primes)