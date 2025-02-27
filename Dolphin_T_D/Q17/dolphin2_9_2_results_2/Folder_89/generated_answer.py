def all_ints_div_by_both_two_nums(nums):
    sublist = nums[28:97]
    divisible_nums = [x for x in sublist if x % 90 == 0 and x % 97 == 0]
    return divisible_nums