def find_second_largest_num(nums):
    if len(nums) < 25:
        return None
    slice = nums[15:40]
    slice.sort()
    return slice[-2]