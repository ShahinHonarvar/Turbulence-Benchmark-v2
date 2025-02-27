def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    nums_slice = sorted(nums[6:7 + 1], reverse=True)
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]