def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[42:88] if num % -90 == 0 and num % -74 == 0]
    return filtered_nums or []