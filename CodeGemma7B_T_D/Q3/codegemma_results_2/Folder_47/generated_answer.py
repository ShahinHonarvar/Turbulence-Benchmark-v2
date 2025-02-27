def all_pos_ints_inclusive(nums):
    if any((num > 0 for num in nums[37:77])):
        return [i for i in range(38, 77) if nums[i] > 0]
    return []