def composite_nums_between_indices(nums):
    result = set()
    for i in range(5, 8):
        if i >= len(nums):
            break
        if not is_prime(nums[i]):
            result.add(nums[i])
    return result