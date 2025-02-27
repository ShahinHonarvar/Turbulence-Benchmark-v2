def all_pos_ints_exclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 25 < num < 80:
            result.append(num)
    return result if result else []