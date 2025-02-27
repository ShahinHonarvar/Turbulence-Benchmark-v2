def find_second_largest_num(nums):
    nums_slice = nums[30:88]
    sorted_nums = sorted(nums_slice, reverse=True)
    if len(sorted_nums) >= 2:
        return sorted_nums[1]
    else:
        return None