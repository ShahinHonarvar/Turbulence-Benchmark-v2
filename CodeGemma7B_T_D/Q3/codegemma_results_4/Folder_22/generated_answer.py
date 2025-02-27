def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if 40 <= num <= 200 and num > 0:
            result.append(num)
    return result