def find_second_smallest_num(num_list):
    if len(num_list) < 10:
        return None
    else:
        sublist = num_list[8:10]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]