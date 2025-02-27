def find_second_smallest_num(nums):
    if len(nums) > 10:
        sublist = nums[10:11]
        if len(sublist) >= 2:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
    return None