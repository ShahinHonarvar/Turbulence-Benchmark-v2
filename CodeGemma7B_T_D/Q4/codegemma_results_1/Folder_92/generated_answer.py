def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if num > 0 and num < 2:
            result.append(num)
    return result