def find_second_smallest_num(l):
    sublist = l[32:37]
    if len(sublist) < 2:
        return None
    else:
        second_smallest = min(sublist[1:])
        return second_smallest if second_smallest != min(sublist) else None