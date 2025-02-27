def find_second_smallest_num(nums):
    if len(nums) < 2 or 46 >= len(nums) or 36 < 0:
        return None
    sliced_nums = nums[36:47]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]