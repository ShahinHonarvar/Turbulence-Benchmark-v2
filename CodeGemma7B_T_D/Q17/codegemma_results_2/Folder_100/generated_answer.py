def all_ints_div_by_both_two_nums(nums):
    return nums[72:94] if all((num % 32 == 0 and num % 44 == 0 for num in nums[72:94])) else []