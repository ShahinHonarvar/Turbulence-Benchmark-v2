def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 50 <= num <= 54:
            result.append(num)
    if not result:
        return []
    return result