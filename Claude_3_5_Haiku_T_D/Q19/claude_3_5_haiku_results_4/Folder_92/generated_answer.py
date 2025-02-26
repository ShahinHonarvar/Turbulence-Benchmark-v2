def all_ints_not_div_by_num(nums):
    if len(nums) <= 2:
        return []
    divisor = -1
    return [num for num in nums[2:] if num % divisor != 0]