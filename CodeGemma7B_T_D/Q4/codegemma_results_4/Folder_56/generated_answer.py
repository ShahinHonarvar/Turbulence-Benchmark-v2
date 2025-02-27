def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if 7 < num < 9 and num > 0:
            result.append(num)
    return result