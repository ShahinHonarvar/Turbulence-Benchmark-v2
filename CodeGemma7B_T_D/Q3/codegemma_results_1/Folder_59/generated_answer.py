def all_pos_ints_inclusive(nums):
    result = []
    for num in nums:
        if num >= 0:
            for i in range(num, 10):
                result.append(i)
    return result