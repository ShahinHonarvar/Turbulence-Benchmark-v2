def find_primes_between_indices(nums):
    prime_nums = []
    for i in range(32, 36):
        if is_prime(nums[i]):
            prime_nums.append(nums[i])
    prime_nums.sort()
    return prime_nums