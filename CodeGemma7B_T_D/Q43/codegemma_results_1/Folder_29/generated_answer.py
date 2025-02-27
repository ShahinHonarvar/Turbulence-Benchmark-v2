def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[24:33]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True) if prime_nums else []