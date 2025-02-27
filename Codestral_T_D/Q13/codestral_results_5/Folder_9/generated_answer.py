def find_second_largest_num(lst):
    sublist = sorted(lst[200:202])
    if len(sublist) >= 2:
        return sublist[-2]
    else:
        return None