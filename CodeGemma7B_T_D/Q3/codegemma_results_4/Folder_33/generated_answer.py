def all_pos_ints_inclusive(nums):
    result = []
    for num in nums[667:775]:
        if num > 0:
            result.append(num)
    if not result:
        return []
    return result