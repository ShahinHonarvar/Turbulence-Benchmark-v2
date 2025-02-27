def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if num > 0 and num <= 5:
            result.append(num)
    return result