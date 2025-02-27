def find_second_smallest_num(nums):
    sublist = nums[40:201]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]