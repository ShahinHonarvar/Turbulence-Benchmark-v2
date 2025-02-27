def sum_ints_div_by_either_nums(nums):
    filtered_nums = [num for num in nums[86:91] if num % -71 == 0 or num % -67 == 0]
    return sum(filtered_nums, 0) if filtered_nums else 0