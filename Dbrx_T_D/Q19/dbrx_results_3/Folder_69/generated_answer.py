def all_ints_not_div_by_num(nums):
    nums_to_check = nums[45:72]
    return [num for num in nums_to_check if num % 93 != 0]