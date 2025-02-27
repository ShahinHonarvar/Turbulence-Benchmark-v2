def sum_ints_div_by_either_nums(nums):
    result = sum((num for num in nums[42:88] if num % -90 == 0 or num % -74 == 0)) or 0
    return result