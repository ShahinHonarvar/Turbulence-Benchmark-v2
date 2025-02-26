def all_ints_div_by_num(nums):
    if len(nums) <= 23:
        return []
    result = [num for num in [nums[23]] if num % -57 == 0]
    return result