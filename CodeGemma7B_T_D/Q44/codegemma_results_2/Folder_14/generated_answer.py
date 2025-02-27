def composite_nums_between_indices(nums):
    result = set()
    for i in range(4, len(nums) - 3):
        if not is_prime(nums[i]):
            result.add(nums[i])
    return result