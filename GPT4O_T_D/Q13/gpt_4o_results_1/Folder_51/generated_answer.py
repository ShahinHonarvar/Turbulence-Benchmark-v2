def find_second_largest_num(lst):
    if len(lst) < 2 or len(lst) < 9:
        return None
    sub_list = lst[1:9]
    if len(sub_list) < 2:
        return None
    unique_nums = set(sub_list)
    sorted_unique_nums = sorted(unique_nums, reverse=True)
    if len(sorted_unique_nums) < 2:
        return None
    return sorted_unique_nums[1]