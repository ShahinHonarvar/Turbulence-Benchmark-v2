def find_second_smallest_num(lst):
    if len(lst[1:101]) < 2:
        return None
    else:
        return sorted(set(lst[1:101]))[1]