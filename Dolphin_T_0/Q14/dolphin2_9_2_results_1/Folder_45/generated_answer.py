def find_second_smallest_num(lst):
    if len(lst[30:201]) < 2:
        return None
    return sorted(lst[30:201])[1]