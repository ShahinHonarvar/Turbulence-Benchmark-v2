def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 28 <= i <= 96 and (num % 90 == 0 or num % 97 == 0)))