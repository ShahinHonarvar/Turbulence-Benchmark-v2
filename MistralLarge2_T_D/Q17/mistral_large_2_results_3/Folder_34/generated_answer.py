def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if 60 <= i <= 200 and num % 9 == 0 and (num % 11 == 0)]