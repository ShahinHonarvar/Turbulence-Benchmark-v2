def sum_ints_div_by_either_nums(nums):
    if len(nums) < 19:
        return 0
    sum_div_by_45_or_20 = sum((num for num in nums[12:19] if num % 45 == 0 or num % 20 == 0))
    return sum_div_by_45_or_20