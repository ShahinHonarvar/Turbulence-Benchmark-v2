def all_ints_not_div_by_num(nums):
    if len(nums) <= 3:
        return []
    result = [num for num in nums[1:-1] if num % 8 != 0]
    return result