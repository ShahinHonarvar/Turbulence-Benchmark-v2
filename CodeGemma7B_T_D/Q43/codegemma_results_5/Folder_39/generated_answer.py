def find_primes_between_indices(nums):
    prime_nums = []
    for num in nums[69:81]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            prime_nums.append(num)
    return sorted(prime_nums) if prime_nums else []