def find_second_smallest_num(nums):
    sub_list = nums[62:79]
    if len(sub_list) < 2:
        return None
    unique_sublist = list(set(sub_list))
    unique_sublist.sort()
    return unique_sublist[1] if len(unique_sublist) > 1 else None