def all_ints_div_by_both_two_nums(nums):
    result = [x for x in nums[18:53] if x % 15 == 0 and x % 57 == 0]
    return result if result else []