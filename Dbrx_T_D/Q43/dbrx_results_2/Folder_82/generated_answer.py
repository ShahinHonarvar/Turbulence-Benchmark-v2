def find_primes_between_indices(numbers):
    primes = []
    for i in range(25, 73):
        if numbers[i] > 1:
            for j in range(2, numbers[i]):
                if numbers[i] % j == 0:
                    break
            else:
                primes.append(numbers[i])
    return sorted(primes)