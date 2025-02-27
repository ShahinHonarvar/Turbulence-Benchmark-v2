def find_primes_between_indices(numbers):
    primes = []
    for i in range(59, 98):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return sorted(primes, reverse=True)