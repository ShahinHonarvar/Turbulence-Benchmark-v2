def find_second_largest_num(nums):
    sublist = nums[75:95]
    if len(set(sublist)) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist, reverse=True)
        return sorted_sublist[1]