def sum_ints_div_by_either_nums(nums):
    subset = nums[7:10]
    total = sum((num for num in subset if num % 2 == 0 or num % 3 == 0))
    return total