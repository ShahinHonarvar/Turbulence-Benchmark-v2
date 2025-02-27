def sum_ints_div_by_either_nums(nums):
    if len(nums) < 80:
        return 0
    return sum((num for num in nums[10:80] if num % 74 == 0 or num % 58 == 0))