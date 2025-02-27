def find_second_smallest_num(lst):
    if not 30 <= len(lst) <= 87:
        return None
    elif len(set(lst[30:88])) < 2:
        return None
    else:
        return sorted(lst[30:88])[1]