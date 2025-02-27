def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if 100 < num < 200:
            result.append(num)
    return result