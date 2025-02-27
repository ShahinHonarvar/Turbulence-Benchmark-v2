def find_second_largest_num(num_list):
    sublist = num_list[5:7]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[-2]