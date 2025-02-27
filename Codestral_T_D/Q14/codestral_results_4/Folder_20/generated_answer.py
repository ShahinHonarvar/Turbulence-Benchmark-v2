def find_second_smallest_num(nums):
    sublist = sorted(nums[75:95])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]