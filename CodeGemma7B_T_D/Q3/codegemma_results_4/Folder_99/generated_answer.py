def all_pos_ints_inclusive(nums):
    result = []
    for num in nums[310:371]:
        if num > 0:
            result.append(num)
    if not result:
        result = []
    return result