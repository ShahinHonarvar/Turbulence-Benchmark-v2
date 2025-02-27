def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sliced_nums = sorted(nums[1:6])
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]