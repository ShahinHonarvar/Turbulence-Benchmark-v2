def all_pos_ints_exclusive(nums):
    result = []
    for n in nums:
        if n > 0 and 73 < nums.index(n) < 84:
            result.append(n)
    return result