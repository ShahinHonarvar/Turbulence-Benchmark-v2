def find_second_smallest_num(lst):
    if len(lst) >= 6 and max(lst[6:9]) != lst[6]:
        return sorted(lst[6:9])[1]
    else:
        return None