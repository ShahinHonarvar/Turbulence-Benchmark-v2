def find_second_smallest_num(nums):
    if len(nums) < 2 or 57 >= len(nums):
        return None
    sliced_nums = nums[56:58]
    sliced_nums.sort()
    if len(sliced_nums) < 2:
        return None
    return sliced_nums[1]