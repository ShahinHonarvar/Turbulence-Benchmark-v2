def find_second_largest_num(num_list):
    if len(num_list) < 69:
        return None
    sublist = num_list[42:69]
    if len(sublist) < 2:
        return None
    sublist.sort(reverse=True)
    return sublist[1]