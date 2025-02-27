def find_second_largest_num(num_list):
    if len(num_list) < 49:
        return None
    sublist = num_list[30:49]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]