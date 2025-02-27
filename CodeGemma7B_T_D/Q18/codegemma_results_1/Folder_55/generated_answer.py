def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[0:10] if num % 10 in (0, 10) or num % 100 == 0)) or 0