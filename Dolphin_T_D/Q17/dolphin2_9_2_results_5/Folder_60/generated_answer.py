def all_ints_div_by_both_two_nums(nums):
    divisible_nums = [num for num in nums[10:80] if num % -74 == 0 and num % -58 == 0]
    return divisible_nums if divisible_nums else []