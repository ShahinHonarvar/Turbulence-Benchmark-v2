def all_ints_div_by_both_two_nums(nums):
    return [num for idx, num in enumerate(nums) if 40 <= idx <= 200 and num % 21 == 0 and (num % 71 == 0)]