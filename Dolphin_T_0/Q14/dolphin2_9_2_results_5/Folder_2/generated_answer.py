def find_second_smallest_num(my_list):
    sublist = my_list[42:87]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]