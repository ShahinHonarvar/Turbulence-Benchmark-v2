def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) <= 4:
        return None
    sublist = nums[:5]
    sorted_sublist = sorted(set(sublist), reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]