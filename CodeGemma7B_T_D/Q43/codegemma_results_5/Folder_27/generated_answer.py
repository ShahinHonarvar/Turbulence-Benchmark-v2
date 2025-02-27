def find_primes_between_indices(nums):
    primes = []
    for num in nums[11:12]:
        if num in [0, 1]:
            continue
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                break
        else:
            primes.append(num)
    return sorted(primes)