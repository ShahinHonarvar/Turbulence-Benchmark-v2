def find_second_largest_num(nums):
    if len(nums) < 66:
        return None
    slice = nums[56:67]
    if len(slice) < 2:
        return None
    return sorted(set(slice))[-2]