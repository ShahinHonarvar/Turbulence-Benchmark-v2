def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    nums_slice = nums[1:9]
    nums_slice.sort()
    if len(nums_slice) < 2:
        return None
    return nums_slice[-2]