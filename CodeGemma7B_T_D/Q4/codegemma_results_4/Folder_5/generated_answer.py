def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if 2 <= num < 7 and num > 0:
            result.append(num)
    return result