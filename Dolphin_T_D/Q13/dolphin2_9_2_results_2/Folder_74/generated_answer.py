def find_second_largest_num(lst):
    sublist = lst[17:79]
    if len(sublist) == 1 or len(set(sublist)) == 1:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[-2]