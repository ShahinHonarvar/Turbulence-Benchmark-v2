def all_ints_not_div_by_num(nums, start=81, end=86):
    return [num for num in nums[start:end] if num % 77 != 0]