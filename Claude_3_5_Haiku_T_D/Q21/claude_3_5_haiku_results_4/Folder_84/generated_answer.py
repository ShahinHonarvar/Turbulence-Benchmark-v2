def all_ints_div_by_num(nums):
    if len(nums) < 54:
        return []
    return [num for num in nums[52:54] if num % 93 == 0]