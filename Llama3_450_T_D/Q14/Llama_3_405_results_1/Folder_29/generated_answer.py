def find_second_smallest_num(nums):
    if len(nums) < 98 or 55 > len(nums):
        return None
    sliced_nums = sorted(nums[55:99])
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]