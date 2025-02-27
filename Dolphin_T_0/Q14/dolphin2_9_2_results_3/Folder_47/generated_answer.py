def find_second_smallest_num(num_list):
    if 63 >= len(num_list) >= 22:
        sublist = num_list[22:64]
        sub_min = min(sublist)
        sublist.remove(sub_min)
        if sublist:
            return min(sublist)
    return None