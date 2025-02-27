def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if num > 0 and nums.index(num) in range(30, 88):
            result.append(num)
    return result