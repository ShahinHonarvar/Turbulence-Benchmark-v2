def find_second_largest_num(nums):
    sublist = nums[80:201]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]