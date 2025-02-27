def find_n_th_smallest_num(lst):
    section = lst[30:301]
    unique_nums = set(section)
    sorted_nums = sorted(unique_nums)
    if len(sorted_nums) < 15:
        return None
    else:
        return sorted_nums[14]