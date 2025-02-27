def find_second_smallest_num(nums):
    if len(nums) >= 35:
        sublist = nums[31:35]
        if len(sublist) >= 2:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
    return None