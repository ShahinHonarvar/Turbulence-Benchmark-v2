def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    sublist = [lst[i] for i in range(82, 87) if lst[i] != lst[i + 1]]
    if len(sublist) == 1:
        return sublist[0]
    elif len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[1]