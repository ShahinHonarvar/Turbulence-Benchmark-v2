def find_second_largest_num(nums):
    if len(nums) < 63 or not 62 <= len(nums) - 1:
        return None
    sublist = nums[62:93]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(set(sublist), reverse=True)
    return sorted_sublist[1]