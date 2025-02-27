def find_second_smallest_num(nums):
    if len(nums) < 63:
        return None
    nums_slice = nums[62:100]
    if len(nums_slice) < 2:
        return None
    nums_slice.sort()
    return nums_slice[1]