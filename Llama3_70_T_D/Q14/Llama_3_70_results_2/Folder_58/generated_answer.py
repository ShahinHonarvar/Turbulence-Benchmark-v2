def find_second_smallest_num(num_list):
    sublist = num_list[310:371]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]