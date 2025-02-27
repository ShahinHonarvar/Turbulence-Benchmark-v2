def all_pos_ints_inclusive(nums):
    result = []
    for num in nums[30:49]:
        if num >= 1:
            result.append(num)
    return result if result else []