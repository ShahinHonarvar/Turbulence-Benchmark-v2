def sum_ints_div_by_either_nums(nums):
    return sum((num for i, num in enumerate(nums) if 38 <= i <= 81 and (num % -61 == 0 or num % -71 == 0)))