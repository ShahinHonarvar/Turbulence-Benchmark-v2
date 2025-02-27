def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[6:10] if num % -1 == 0 and num % -10 == 0]
    return filtered_nums