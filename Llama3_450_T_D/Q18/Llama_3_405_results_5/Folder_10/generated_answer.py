def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 32 <= i <= 99 and (num % -11 == 0 or num % -15 == 0)))