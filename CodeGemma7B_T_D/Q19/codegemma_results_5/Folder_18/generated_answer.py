def all_ints_not_div_by_num(nums):
    result = [num for num in nums[35:98] if num % 41 != 0]
    return result or []