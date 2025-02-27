def all_pos_ints_exclusive(nums):
    result = []
    for num in nums[276:376]:
        if num > 0:
            result.append(num)
    return result