def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if 0 <= num <= 1:
            result.append(num)
    return result