def find_second_largest_num(nums):
    sublist = nums[20:31]
    set_list = set(sublist)
    if len(set_list) < 2:
        return None
    set_list.remove(max(set_list))
    return max(set_list)