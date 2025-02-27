def all_ints_div_by_both_two_nums(nums):
    nums = nums[38:53]
    return [num for num in nums if num % -41 == 0 and num % -47 == 0]