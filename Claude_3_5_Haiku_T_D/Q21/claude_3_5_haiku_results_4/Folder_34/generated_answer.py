def all_ints_div_by_num(nums):
    if len(nums) <= 30:
        return []
    return [num for num in nums[30:31] if num % 3 == 0]