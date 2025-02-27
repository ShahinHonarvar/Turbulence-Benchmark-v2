def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[0:10] if num % 6 == 0 or num % -3 == 0)) or 0