def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[55:80 + 1] if num % 22 == 0 or num % 32 == 0)) or 0