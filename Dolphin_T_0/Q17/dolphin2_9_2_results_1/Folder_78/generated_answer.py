def all_ints_div_by_both_two_nums(nums):
    result = [num for i, num in enumerate(nums) if i >= 34 and i <= 69 and (num % 19 == 0) and (num % 32 == 0)]
    return result