def all_ints_not_div_by_num(nums):
    if len(nums) <= 16:
        return []
    return [num for num in nums[16:92] if num % 59 != 0]