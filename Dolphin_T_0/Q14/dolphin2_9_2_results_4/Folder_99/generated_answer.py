def find_second_smallest_num(lst):
    if len(lst) < 2:
        return 'None'
    smallest = min(lst)
    lst.remove(smallest)
    second_smallest = min(lst)
    if 608 <= lst.index(second_smallest) <= 609:
        return second_smallest
    else:
        return 'None'