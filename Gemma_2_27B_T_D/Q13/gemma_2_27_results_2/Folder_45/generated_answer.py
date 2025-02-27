def find_second_largest_num(nums):
    nums_slice = nums[30:201]
    if len(nums_slice) < 2:
        return None
    sorted_nums = sorted(nums_slice)
    return sorted_nums[-2]