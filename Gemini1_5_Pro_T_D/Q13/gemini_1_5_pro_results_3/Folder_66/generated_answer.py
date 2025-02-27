def find_second_largest_num(nums):
    sublist = nums[50:55]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2]