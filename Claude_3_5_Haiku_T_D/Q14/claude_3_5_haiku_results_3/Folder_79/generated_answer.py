def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sublist = nums[1:6]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]