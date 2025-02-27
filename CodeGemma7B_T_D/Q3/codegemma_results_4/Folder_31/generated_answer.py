def all_pos_ints_inclusive(nums):
    result = []
    if any((x > 0 for x in nums[75:89])):
        for num in nums[75:89]:
            if num > 0:
                result.append(num)
    return result