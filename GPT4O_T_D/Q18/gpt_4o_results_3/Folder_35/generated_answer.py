def sum_ints_div_by_either_nums(nums):
    if len(nums) < 88:
        return 0
    return sum((num for num in nums[77:88] if num % 23 == 0 or num % 57 == 0))