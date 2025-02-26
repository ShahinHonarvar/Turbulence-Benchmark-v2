def all_ints_not_div_by_num(nums):
    if len(nums) <= 10:
        return []
    result = [num for num in nums[9:10] if num % 8 != 0]
    return result