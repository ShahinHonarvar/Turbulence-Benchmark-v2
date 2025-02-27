def sum_ints_div_by_either_nums(nums):
    if len(nums) >= 71:
        return sum((num for num in nums[69:71] if num % 72 == 0 or num % 70 == 0))
    return 0