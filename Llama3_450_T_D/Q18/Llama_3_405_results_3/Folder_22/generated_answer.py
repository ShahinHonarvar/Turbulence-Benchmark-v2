def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 40 <= i <= 200 and (num % 21 == 0 or num % 71 == 0)))