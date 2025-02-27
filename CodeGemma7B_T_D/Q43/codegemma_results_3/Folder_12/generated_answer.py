def find_primes_between_indices(nums):
    primes = []
    for num in nums[16:26]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    return sorted(primes, reverse=True)