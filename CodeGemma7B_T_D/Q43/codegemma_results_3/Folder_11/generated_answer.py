def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[55:77 + 1]:
        if is_prime(num) and num not in prime_nums:
            prime_nums.append(num)
    return sorted(prime_nums)