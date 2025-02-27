def find_second_smallest_num(nums):
    if len(nums) < 96:
        return None
    sliced_nums = nums[75:95]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]