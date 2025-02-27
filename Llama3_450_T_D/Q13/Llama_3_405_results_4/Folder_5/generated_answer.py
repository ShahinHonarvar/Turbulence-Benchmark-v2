def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    nums_slice = nums[8:10]
    if len(nums_slice) < 2:
        return None
    return sorted(nums_slice)[-2]