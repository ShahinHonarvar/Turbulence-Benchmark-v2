def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sublist = nums[:4]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]