def all_pos_ints_inclusive(nums):
    result = []
    low = 22
    hi = 88
    for num in nums:
        if num > 0 and low <= num <= hi:
            result.append(num)
    return result