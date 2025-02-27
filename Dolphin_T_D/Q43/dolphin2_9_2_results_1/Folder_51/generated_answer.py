def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[14:69]:
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)
    return sorted(primes, reverse=True)