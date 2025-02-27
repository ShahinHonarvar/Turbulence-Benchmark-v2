def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 42 <= i <= 43 and (num % 15 == 0 or num % 87 == 0)))