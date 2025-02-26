def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sublist = nums[1:9]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    return sorted_sublist[1]