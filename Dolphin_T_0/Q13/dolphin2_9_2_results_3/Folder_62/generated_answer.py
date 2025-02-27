def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    sublist = lst[90:100]
    if len(set(sublist)) < 2:
        return None
    sorted_sublist = sorted(sublist, reverse=True)
    if sorted_sublist[0] != sorted_sublist[1]:
        return sorted_sublist[1]
    else:
        for i in range(2, len(sorted_sublist)):
            if sorted_sublist[i] != sorted_sublist[1]:
                return sorted_sublist[i]
        return None