def find_primes_between_indices(numbers):
    primes = []
    for i in range(min(20, len(numbers)), min(49, len(numbers))):
        is_prime = True
        if numbers[i] < 2:
            continue
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)