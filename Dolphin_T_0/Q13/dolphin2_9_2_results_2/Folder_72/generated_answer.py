def find_second_largest_num(num_list):
    if 51 < len(num_list) < 29:
        return None
    else:
        sublist = num_list[29:52]
        if len(sublist) < 2:
            return None
        else:
            sublist.sort(reverse=True)
            return sublist[1]