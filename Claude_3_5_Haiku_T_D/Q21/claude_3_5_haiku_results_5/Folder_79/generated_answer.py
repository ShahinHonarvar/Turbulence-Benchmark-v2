def all_ints_div_by_num(nums):
    if len(nums) < 9:
        return []
    result = [num for num in [nums[8]] if num % -7 == 0]
    return result