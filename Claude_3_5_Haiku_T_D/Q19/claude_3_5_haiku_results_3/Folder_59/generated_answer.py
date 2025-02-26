def all_ints_not_div_by_num(nums):
    return [num for num in nums[9:] if num not in nums[8:9] and num % 8 != 0]