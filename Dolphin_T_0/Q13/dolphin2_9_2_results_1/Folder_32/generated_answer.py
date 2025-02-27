def find_second_largest_num(lst):
    if len(lst) < 98:
        return None
    else:
        sublist = lst[21:98]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            i = 1
            while sublist[i] == sublist[0] and i < len(sublist):
                i = i + 1
            if i == len(sublist):
                return None
            else:
                return sublist[i]