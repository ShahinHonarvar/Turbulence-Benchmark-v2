def find_second_smallest_num(lst):
    if not lst:
        return None
    lst.sort()
    for i in range(22, 51):
        if i < len(lst):
            return lst[i]