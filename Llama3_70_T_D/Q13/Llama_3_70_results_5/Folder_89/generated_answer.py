def find_second_largest_num(lst):
    if len(lst) < 83:
        return None
    num_list = lst[56:83]
    if len(set(num_list)) < 2:
        return None
    return sorted(set(num_list))[-2]