def all_ints_not_div_by_num(nums):
    if len(nums) <= 95:
        return []
    result = [num for num in nums[94:-1] if num % 57 != 0]
    return result