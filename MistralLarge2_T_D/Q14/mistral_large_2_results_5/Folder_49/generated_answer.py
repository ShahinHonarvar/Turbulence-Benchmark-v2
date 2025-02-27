def find_second_smallest_num(lst):
    if len(lst) < 201:
        return None
    sublist = lst[80:201]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    return second_smallest