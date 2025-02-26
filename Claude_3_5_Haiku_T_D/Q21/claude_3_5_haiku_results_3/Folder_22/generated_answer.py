def all_ints_div_by_num(nums):
    if len(nums) <= 10:
        return []
    result = [num for num in [nums[10]] if num % 1 == 0]
    return result