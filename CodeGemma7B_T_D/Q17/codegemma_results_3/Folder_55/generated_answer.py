def all_ints_div_by_both_two_nums(nums):
    return [num for num in nums if num % 10 == 0 and num % 100 == 0 and (num >= 0) and (num <= 9)]