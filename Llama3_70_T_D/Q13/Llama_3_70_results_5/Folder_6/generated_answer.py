def find_second_largest_num(nums):
    if len(nums) < 67:
        return None
    nums_slice = nums[10:67]
    if len(set(nums_slice)) < 2:
        return None
    return sorted(set(nums_slice), reverse=True)[1]