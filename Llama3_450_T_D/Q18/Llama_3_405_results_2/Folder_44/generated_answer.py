def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 25 <= i <= 70 and (num % 74 == 0 or num % 15 == 0)))