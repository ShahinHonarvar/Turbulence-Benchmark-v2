def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sliced_nums = nums[15:52]
    if len(sliced_nums) < 2:
        return None
    sorted_nums = sorted(sliced_nums, reverse=True)
    return sorted_nums[1]