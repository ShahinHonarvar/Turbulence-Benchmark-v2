def find_second_smallest_num(nums):
    if 262 <= len(nums) <= 746:
        sublist = nums[262:746]
        sorted_sublist = sorted(sublist)
        if len(sorted_sublist) > 1:
            return sorted_sublist[1]
    return None