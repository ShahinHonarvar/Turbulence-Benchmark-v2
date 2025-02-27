def all_ints_not_div_by_num(nums):
    if len(nums) <= 70:
        return []
    return [num for num in nums[71:200] if num % -300 != 0]