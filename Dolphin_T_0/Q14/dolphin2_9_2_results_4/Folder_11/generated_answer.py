def find_second_smallest_num(lst):
    if lst[66:94]:
        sorted_lst = sorted(lst[66:94])
        if len(sorted_lst) > 1:
            return sorted_lst[1]
        else:
            return 'None'
    else:
        return 'None'