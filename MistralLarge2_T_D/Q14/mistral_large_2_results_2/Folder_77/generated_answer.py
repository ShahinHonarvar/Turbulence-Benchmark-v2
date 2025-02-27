def find_second_smallest_num(nums):
    if len(nums) <= 639 or len(nums) <= 975:
        return None
    sublist = nums[639:976]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]