def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 48 < num < 74:
            result.append(num)
    return result