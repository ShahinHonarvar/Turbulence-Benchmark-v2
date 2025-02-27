def find_second_largest_num(lst):
    sublist = lst[27:56]
    if len(set(sublist)) < 2:
        return None
    else:
        return sorted(set(sublist))[-2]