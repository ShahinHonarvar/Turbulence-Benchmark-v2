def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[29:46] if num % 27 == 0 and num % 81 == 0]
    return result