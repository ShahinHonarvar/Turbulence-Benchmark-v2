def sum_ints_div_by_either_nums(nums):
    return sum((num for idx, num in enumerate(nums[34:82]) if num % 27 == 0 or num % 57 == 0))