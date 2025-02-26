def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[90:201] if num % -31 == 0 and num % 13 == 0]
    return result