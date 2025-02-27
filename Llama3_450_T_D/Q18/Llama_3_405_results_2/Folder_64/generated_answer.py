def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums[:4]) if num % 11 == 0 or num % -7 == 0))