def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if 90 < num < 200 and num not in result:
            result.append(num)
    return result