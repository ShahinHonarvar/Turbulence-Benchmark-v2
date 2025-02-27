def find_second_smallest_num(nums):
    if len(nums) > 28:
        sublist = nums[28:39]
        if len(sublist) > 1:
            sorted_sublist = sorted(set(sublist))
            if len(sorted_sublist) > 1:
                return sorted_sublist[1]
    return None