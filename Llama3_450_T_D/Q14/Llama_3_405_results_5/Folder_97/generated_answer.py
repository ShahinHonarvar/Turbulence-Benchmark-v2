def find_second_smallest_num(nums):
    if len(nums) < 35:
        return None
    nums_slice = sorted(nums[31:35])
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]