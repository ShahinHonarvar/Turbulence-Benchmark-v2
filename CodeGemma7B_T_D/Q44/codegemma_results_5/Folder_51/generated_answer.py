def composite_nums_between_indices(nums):
    return {num for num in nums[1:9] if not isprime(num)}