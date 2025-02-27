def find_second_smallest_num(lst):
    if len(lst) < 201 or 80 > len(lst):
        return None
    sublist = lst[80:201]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]