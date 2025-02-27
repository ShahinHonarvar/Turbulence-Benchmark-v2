def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 70 < num < 98:
            result.append(num)
    return result