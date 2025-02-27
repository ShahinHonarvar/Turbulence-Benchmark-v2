def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 20 <= i <= 35 and (num % -36 == 0 or num % -89 == 0)))