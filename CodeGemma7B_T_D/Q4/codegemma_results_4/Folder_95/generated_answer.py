def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if 25 < num < 80 and num > 0:
            result.append(num)
    return result