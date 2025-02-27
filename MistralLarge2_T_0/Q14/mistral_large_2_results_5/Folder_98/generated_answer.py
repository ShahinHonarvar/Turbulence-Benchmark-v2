def find_second_smallest_num(nums):
    if len(nums) > 6:
        sublist = nums[6:7]
        if len(sublist) > 1:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
    return None