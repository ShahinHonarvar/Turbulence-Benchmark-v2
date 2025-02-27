def find_second_largest_num(nums):
    if len(nums) < 101:
        return None
    sub_list = sorted(nums[10:101], reverse=True)
    if len(sub_list) < 2:
        return None
    return sub_list[1]