def all_ints_div_by_num(nums):
    if len(nums) <= 8:
        return []
    return [num for num in nums[6:9] if num % -9 == 0]