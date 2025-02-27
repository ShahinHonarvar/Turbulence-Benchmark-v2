def find_second_largest_num(nums):
    if len(nums) > 746:
        sublist = nums[262:747]
        if len(sublist) >= 2:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[-2]
    return None