def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums[0:4] if num % 11 == 0 and num % -7 == 0]