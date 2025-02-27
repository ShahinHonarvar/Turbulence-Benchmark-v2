def sum_ints_div_by_either_nums(nums):
    result = sum((num for num in nums[40:201] if num % 21 == 0 or num % 71 == 0))
    return result if result else 0