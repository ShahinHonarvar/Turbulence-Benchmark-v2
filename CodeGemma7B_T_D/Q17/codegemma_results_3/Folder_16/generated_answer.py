def all_ints_div_by_both_two_nums(nums):
    result = [i for i in nums[55:81] if i % 22 == 0 and i % 32 == 0]
    return result or []