def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[2:8] if num % -1 == 0 or num % -7 == 0))