def find_primes_between_indices(nums):
    primes = []
    for i in range(413, 448):
        if all((nums[j] % i != 0 for j in range(1, i // 2))):
            primes.append(i)
    return sorted(primes)