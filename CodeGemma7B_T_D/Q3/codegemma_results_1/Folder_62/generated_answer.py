def all_pos_ints_inclusive(nums):
    result = []
    for num in range(91, 100):
        if num in nums:
            result.append(num)
    return result