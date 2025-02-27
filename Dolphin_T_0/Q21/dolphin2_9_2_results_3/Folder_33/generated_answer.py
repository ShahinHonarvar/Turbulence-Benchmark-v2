def all_ints_div_by_num(nums):
    result = [num for num in nums[319:613] if num % -215 == 0]
    return result if result else []