def all_ints_not_div_by_num(nums):
    if len(nums) < 4:
        return []
    return [num for num in nums[2:3] if num % 5 != 0]