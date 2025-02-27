def find_second_smallest_num(lst):
    try:
        sublist = lst[661:925]
        min1 = min(sublist)
        sublist.remove(min1)
        min2 = min(sublist)
        return min2
    except ValueError:
        return None