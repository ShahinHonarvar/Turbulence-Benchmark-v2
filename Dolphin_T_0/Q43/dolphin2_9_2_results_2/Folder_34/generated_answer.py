def find_primes_between_indices(numbers):
    primes = []
    for number in numbers[56:58]:
        if all((number % i != 0 for i in range(2, number))):
            primes.append(number)
    return sorted(primes, reverse=True) or []