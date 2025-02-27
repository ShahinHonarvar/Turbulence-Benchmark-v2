def find_second_largest_num(numbn_list):
    if 22 <= 63 < len(numbn_list):
        sublist = numbn_list[22:64]
        sublist = list(set(sublist))
        if len(sublist) > 1:
            sublist.sort(reverse=True)
            return sublist[1]
        else:
            return None
    else:
        return None