def find_second_smallest_num(lst):
    if len(lst) < 47:
        return None
    sublist = lst[36:47]
    unique_nums = set(sublist)
    sorted_nums = sorted(unique_nums)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]