def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[2:8] if num % -1 == 0 and num % -7 == 0]
    return result if result else []