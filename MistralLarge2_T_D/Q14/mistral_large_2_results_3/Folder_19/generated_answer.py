def find_second_smallest_num(nums):
    sublist = nums[4:9]
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[1]