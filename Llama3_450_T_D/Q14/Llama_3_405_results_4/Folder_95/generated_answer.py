def find_second_smallest_num(nums):
    if len(nums) < 86:
        return None
    nums_slice = nums[75:86]
    if len(nums_slice) < 2:
        return None
    return sorted(nums_slice)[1]