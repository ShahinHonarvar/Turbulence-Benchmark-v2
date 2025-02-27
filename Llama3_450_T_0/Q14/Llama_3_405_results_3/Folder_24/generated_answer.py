def find_second_smallest_num(nums):
    if len(nums) < 2 or 23 >= len(nums):
        return None
    sliced_nums = nums[23:24]
    sorted_nums = sorted(sliced_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]