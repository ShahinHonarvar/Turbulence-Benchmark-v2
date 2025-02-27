def find_second_largest_num(nums):
    if len(nums) < 77:
        return None
    sublist = nums[37:77]
    if len(sublist) < 2:
        return None
    unique_nums = set(sublist)
    if len(unique_nums) < 2:
        return None
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[1]