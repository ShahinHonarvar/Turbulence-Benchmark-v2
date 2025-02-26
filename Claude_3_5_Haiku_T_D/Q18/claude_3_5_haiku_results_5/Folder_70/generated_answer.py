def sum_ints_div_by_either_nums(nums):
    if len(nums) < 44:
        return 0
    return sum((num for num in nums[42:44] if num % 15 == 0 or num % 87 == 0))