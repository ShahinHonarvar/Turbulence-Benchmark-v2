def all_ints_div_by_both_two_nums(nums):
    divisible_nums = [num for num in nums[11:47] if num % 55 == 0 and num % 36 == 0]
    return divisible_nums