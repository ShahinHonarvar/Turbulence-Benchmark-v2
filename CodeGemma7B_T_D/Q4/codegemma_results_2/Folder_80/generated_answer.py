def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    result = []
    for num in nums:
        if num > 68 and num < 98:
            result.append(num)
    return result