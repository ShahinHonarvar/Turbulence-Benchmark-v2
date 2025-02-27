def find_primes_between_indices(nums):
    if not nums:
        return []
    primes = []
    for i in range(25, 73):
        if nums[i] % 2 == 0 or nums[i] % 3 == 0 or nums[i] % 5 == 0 or (nums[i] % 7 == 0):
            continue
        is_prime = True
        for j in range(11, int(nums[i] ** 0.5) + 1, 2):
            if nums[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    return sorted(primes)