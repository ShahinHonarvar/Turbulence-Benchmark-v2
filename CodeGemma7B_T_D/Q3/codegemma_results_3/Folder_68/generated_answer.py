def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if num > 0 and 0 <= num <= 8:
            result.append(num)
    return result