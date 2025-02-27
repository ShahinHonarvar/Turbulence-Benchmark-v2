def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[20:200] if num % 20 == 0 or num % 200 == 0)) or 0