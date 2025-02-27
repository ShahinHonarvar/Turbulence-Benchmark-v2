def find_second_smallest_num(lst):
    if len(lst) < 78:
        return None
    num_set = set(lst[66:78])
    if len(num_set) < 2:
        return None
    num_list = sorted(list(num_set))
    return num_list[1]