def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    nums_slice = nums[4:9]
    if len(nums_slice) < 2:
        return None
    nums_slice.sort()
    return nums_slice[-2]