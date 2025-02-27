def find_second_largest_num(nums):
    if len(nums) < 78:
        return None
    slice = nums[62:79]
    if len(slice) < 2:
        return None
    return sorted(slice)[-2]