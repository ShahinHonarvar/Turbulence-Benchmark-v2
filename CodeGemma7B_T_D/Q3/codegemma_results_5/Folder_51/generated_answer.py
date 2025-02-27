def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if 1 <= num <= 8:
            result.append(num)
    return result or []