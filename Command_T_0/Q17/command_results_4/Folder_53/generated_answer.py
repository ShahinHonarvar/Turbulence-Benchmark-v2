def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[200:-200:-1] if x % 17 == 0 and x % -5 == 0]