def all_ints_div_by_both_two_nums(nums):
    result = [num for num in nums[46:92] if num % 67 == 0 and num % 15 == 0]
    return result if result else []