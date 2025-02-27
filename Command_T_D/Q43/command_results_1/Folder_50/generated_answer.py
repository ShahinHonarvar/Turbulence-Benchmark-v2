def find_primes_between_indices(nums):
    primes = []
    for i in range(23, 59):
        if all((n % j != 0 for j in range(2, i // 2 + 1))):
            primes.append(i)
    return primes