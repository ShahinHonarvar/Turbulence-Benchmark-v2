def all_ints_div_by_both_two_nums(nums):
    result = [num for i, num in enumerate(nums[34:82]) if i % 27 == 0 and i % 57 == 0]
    return result