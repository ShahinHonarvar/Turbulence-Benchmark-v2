def sum_ints_div_by_either_nums(nums):
    subset = nums[299:383]
    total = sum((num for num in subset if num % 858 == 0 or num % 952 == 0))
    return total