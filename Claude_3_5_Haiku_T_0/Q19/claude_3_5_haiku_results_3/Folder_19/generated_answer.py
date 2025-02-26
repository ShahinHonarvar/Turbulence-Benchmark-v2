def all_ints_not_div_by_num(nums):
    if len(nums) <= 5:
        return []
    result = [num for num in nums[5:-1] if num % -7 != 0]
    return result