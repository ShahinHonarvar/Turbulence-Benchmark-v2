def find_second_smallest_num(lst):
    if len(lst) < 2 or len(lst[:4]) < 2:
        return None
    sorted_sublist = sorted(lst[:4])
    return sorted_sublist[1]