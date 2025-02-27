def all_ints_div_by_both_two_nums(nums):
    divisible_nums = [num for num in nums[7:8] if num % 5 == 0 and num % 7 == 0]
    return divisible_nums if len(divisible_nums) != 0 else []