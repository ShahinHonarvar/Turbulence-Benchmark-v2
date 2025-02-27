def all_ints_div_by_both_two_nums(nums):
    result = [x for x in nums[0:9] if x % -3 == 0 and x % 8 == 0]
    return result