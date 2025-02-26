def all_ints_not_div_by_num(nums):
    if len(nums) <= 1:
        return []
    divisor = nums[1]
    result = [num for num in nums[2:] if num % divisor != 0]
    return result