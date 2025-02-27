def find_second_largest_num(nums):
    nums_slice = sorted(nums[667:775], reverse=True)
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]