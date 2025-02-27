def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if i in (69, 70) and (num % 72 == 0 or num % 70 == 0)))