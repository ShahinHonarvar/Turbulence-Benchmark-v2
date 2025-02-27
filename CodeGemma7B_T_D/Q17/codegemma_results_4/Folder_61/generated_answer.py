def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[0:7] if num % 5 == 0 and num % 6 == 0]
    return filtered_nums