def find_primes_between_indices(numbers):
    primes = []
    for i in range(61, 81):
        if i < 0 or i >= len(numbers):
            break
        is_prime = True
        for j in range(2, int(numbers[i] ** 0.5) + 1):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime and numbers[i] > 1:
            primes.append(numbers[i])
    return sorted(primes, reverse=True)