def find_primes_between_indices(nums):
    primes = []
    for i in range(478, 950):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            primes.append(i)
    return sorted(primes, reverse=True) or []