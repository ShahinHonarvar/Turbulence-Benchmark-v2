def find_primes_between_indices(numbers):
    primes = []
    for i in range(23, 76):
        n = numbers[i]
        if n < 2:
            continue
        is_prime = True
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return sorted(primes, reverse=True)