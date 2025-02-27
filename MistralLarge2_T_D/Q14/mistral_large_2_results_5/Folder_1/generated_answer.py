def find_second_smallest_num(nums):
    if len(nums) >= 56:
        sublist = nums[34:56]
        if len(set(sublist)) > 1:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
    return None