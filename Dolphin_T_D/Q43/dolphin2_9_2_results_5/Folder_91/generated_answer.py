def find_primes_between_indices(nums):
    primes = []
    for i in range(2, 10):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    break
            else:
                primes.append(nums[i])
    primes.sort()
    return primes