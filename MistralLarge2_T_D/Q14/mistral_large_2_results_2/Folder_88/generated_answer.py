def find_second_smallest_num(lst):
    sublist = lst[6:9]
    if len(sublist) < 2:
        return None
    unique_nums = sorted(set(sublist))
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]