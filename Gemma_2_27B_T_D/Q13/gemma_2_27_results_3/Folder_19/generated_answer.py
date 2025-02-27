def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sublist = nums[3:6]
    if len(set(sublist)) < 2:
        return None
    return sorted(sublist)[-2]