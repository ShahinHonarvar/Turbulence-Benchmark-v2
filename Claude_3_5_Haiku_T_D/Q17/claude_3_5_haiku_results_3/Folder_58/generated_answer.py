def all_ints_div_by_both_two_nums(nums):
    divisible_nums = [num for num in nums[240:902] if num % 546 == 0 and num % 709 == 0]
    return divisible_nums