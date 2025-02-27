def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[13:69]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes)