def find_second_smallest_num(nums):
    if len(nums) < 2 or 51 >= len(nums) or 37 < 0:
        return None
    sliced_nums = nums[37:52]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]