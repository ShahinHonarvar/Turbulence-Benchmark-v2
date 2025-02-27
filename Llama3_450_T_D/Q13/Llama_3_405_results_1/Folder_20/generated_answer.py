def find_second_largest_num(num_list):
    if len(num_list) < 67:
        return None
    sublist = num_list[56:67]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]