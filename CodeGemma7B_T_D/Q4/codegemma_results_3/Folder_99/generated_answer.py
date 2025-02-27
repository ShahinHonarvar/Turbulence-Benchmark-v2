def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if num > 0 and (295 < nums.index(num) and nums.index(num) < 573):
            result.append(num)
    return result