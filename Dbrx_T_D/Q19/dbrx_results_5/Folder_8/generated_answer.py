def all_ints_not_div_by_num(nums):
    start, end = (17, 88)
    return [num for num in nums[start:end] if num % -75 != 0] or []