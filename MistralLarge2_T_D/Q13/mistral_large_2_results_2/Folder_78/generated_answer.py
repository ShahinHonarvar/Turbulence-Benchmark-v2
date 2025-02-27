def find_second_largest_num(nums):
    if len(nums) < 52:
        return None
    sub_list = nums[43:52]
    if len(sub_list) < 2:
        return None
    sub_list = sorted(sub_list, reverse=True)
    return sub_list[1]