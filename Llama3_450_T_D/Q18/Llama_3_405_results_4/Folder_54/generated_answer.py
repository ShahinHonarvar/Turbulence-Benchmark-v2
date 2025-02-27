def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 13 <= i <= 91 and (num % -65 == 0 or num % -62 == 0)))