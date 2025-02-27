def find_second_largest_num(lst):
    if len(lst) < 5:
        return 'None'
    sublist = lst[1:6]
    sublist.sort()
    return sublist[-2] if len(set(sublist)) > 1 else 'None'