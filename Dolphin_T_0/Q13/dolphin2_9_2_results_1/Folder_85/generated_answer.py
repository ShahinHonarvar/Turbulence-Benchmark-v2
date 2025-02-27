def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    else:
        sublist = lst[5:9]
        unique_sublist = list(set(sublist))
        if len(unique_sublist) < 2:
            return None
        else:
            unique_sorted_sublist = sorted(unique_sublist, reverse=True)
            return unique_sorted_sublist[1]