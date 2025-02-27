def find_primes_between_indices(numbers):
    primes = []
    for number in numbers[60:96]:
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            primes.append(number)
    return sorted(primes)