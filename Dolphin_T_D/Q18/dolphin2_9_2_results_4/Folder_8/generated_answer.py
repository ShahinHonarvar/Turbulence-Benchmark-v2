def sum_ints_div_by_either_nums(nums):
    total = sum((num for num in nums[36:86] if num % -27 == 0 or num % -96 == 0))
    return total