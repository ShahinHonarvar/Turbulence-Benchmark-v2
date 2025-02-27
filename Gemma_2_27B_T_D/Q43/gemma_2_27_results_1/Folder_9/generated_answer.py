def find_primes_between_indices(nums):
    result = []
    for i in range(16, 72):
        n = nums[i]
        if n > 1:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    break
            else:
                result.append(n)
    return sorted(result)