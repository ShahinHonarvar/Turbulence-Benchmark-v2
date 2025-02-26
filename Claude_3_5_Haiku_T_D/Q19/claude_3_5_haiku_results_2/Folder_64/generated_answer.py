def all_ints_not_div_by_num(nums):
    if len(nums) <= 3:
        return []
    return [num for num in nums[3:-1] if num % 2 != 0]