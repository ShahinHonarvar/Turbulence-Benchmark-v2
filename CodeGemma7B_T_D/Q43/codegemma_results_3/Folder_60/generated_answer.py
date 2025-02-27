def find_primes_between_indices(nums):
    primes = []
    for i in range(46, 86):
        if all((i % j for j in range(2, i))):
            primes.append(i)
    return sorted(primes) or []