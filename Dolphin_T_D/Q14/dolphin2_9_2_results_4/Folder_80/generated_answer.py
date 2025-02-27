def find_second_smallest_num(lst):
    if len(lst) < 88:
        return 'None'
    else:
        sublist = lst[30:88]
        if not all((i < j for i, j in zip(sublist, sublist[1:]))):
            return 'None'
        else:
            return sorted(sublist)[1]