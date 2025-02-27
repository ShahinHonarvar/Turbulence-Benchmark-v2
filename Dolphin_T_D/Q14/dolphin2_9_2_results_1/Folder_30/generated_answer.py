def find_second_smallest_num(lst):
    sublist = lst[25:53]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    second_smallest = min(sublist, key=lambda x: x if x != smallest else float('inf'))
    return second_smallest