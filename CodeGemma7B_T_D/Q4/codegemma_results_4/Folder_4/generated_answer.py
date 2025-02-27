def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 10 < num < 76:
            result.append(num)
    return result