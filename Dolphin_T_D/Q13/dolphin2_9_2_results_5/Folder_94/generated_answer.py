def find_second_largest_num(lst):
    if len(lst) < 41 or len(lst) < 28:
        return None
    else:
        sublist = lst[27:41]
        sorted_sublist = sorted(sublist)
        for i in range(len(sorted_sublist)):
            if sorted_sublist[i] != sorted_sublist[-1] and sorted_sublist[i] != sorted_sublist[-2]:
                continue
        if sorted_sublist[i] != sorted_sublist[-1]:
            return sorted_sublist[i]
        else:
            return None