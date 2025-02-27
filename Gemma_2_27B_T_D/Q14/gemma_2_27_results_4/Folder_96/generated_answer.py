def find_second_smallest_num(nums):
    if len(nums) < 151 or len(set(nums)) != len(nums):
        return None
    sublist = nums[50:201]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]