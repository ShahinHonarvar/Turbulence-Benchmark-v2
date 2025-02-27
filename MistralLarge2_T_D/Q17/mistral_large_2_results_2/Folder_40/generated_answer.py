def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i in range(2) and num % 2 == 0]