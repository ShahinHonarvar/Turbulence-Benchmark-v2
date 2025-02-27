def find_second_largest_num(nums):
    if len(nums) <= 639:
        return None
    sublist = nums[639:976]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    return max(sublist) if sublist else None