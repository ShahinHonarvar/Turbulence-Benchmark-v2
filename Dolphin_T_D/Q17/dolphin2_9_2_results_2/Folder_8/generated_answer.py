def all_ints_div_by_both_two_nums(nums):
    divisible_numbers = [num for num in nums[36:86] if num % -27 == 0 and num % -96 == 0]
    return divisible_numbers if len(divisible_numbers) > 0 else []