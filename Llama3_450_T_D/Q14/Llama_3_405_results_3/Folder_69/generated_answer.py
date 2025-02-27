def find_second_smallest_num(nums):
    sliced_nums = sorted(nums[25:88])
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]