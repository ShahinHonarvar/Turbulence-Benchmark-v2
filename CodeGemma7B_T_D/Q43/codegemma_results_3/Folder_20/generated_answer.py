def find_primes_between_indices(numbers):
    primes = []
    for i in range(36, 41):
        if all((num % i != 0 for num in numbers)):
            primes.append(i)
    return sorted(primes, reverse=True)