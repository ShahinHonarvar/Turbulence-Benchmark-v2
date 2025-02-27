def find_primes_between_indices(numbers):
    primes = [num for num in numbers[7:10] if num > 1 and all((num % i != 0 for i in range(2, num)))]
    primes.sort(reverse=True)
    return primes