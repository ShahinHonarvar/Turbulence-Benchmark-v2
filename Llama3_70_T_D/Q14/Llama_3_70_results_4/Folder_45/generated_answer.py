def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    return sorted(lst[30:201])[1]