def all_pos_ints_inclusive(nums):
    results = []
    nums = nums[28:33]
    for num in nums:
        if num > 0:
            results.append(num)
    return results if len(results) > 0 else []