def find_second_smallest_num(nums):
    if len(nums) < 49 or len(nums) < 35:
        return None
    sublist = nums[35:50]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]