def find_primes_between_indices(nums):
    primes = []
    for i in range(len(nums)):
        if nums[i] > 1 and i >= 89 and (i <= 93):
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    break
            else:
                primes.append(nums[i])
    return sorted(primes, reverse=True)