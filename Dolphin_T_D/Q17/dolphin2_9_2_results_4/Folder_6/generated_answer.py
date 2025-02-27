def all_ints_div_by_both_two_nums(nums):
    result = [num for i, num in enumerate(nums) if 41 <= i <= 56 and num % 82 == 0 and (num % 90 == 0)]
    return result