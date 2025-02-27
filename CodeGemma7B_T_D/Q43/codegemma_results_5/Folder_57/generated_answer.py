def find_primes_between_indices(numbers):
    primes = []
    for i in range(35, 90):
        if numbers[i] == 2 or (numbers[i] % 2 != 0 and all((numbers[i] % j != 0 for j in range(3, int(numbers[i] ** 0.5) + 1, 2)))):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)