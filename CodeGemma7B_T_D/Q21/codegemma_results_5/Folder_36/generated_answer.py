def all_ints_div_by_num(nums):
    filtered_nums = [num for num in nums[421:490] if num % 885 == 0]
    return filtered_nums or []