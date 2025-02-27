def find_second_smallest_num(lst):
    if len(lst) <= 94:
        return None
    return sorted(lst[75:95])[1]