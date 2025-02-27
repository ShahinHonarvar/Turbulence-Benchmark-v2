def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if 68 <= num <= 86 and num > 0:
            result.append(num)
    return result or []