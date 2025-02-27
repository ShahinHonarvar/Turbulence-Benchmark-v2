def all_ints_div_by_both_two_nums(nums):
    filtered_nums = [num for num in nums[78:82] if num % 76 == 0 and num % 60 == 0]
    return filtered_nums