def find_primes_between_indices(nums):
    primes = []
    for num in nums[239:686]:
        if all((num % k for k in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(set(primes))