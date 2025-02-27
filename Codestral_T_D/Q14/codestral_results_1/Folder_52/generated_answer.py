def find_second_smallest_num(num_list):
    sublist = num_list[64:67]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]