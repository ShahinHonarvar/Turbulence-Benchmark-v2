def find_second_largest_num(lst):
    if len(lst) < 62:
        return None
    sublist = lst[16:62]
    largest = max(sublist)
    second_largest = max((x for x in sublist if x != largest))
    return second_largest if second_largest != largest else None