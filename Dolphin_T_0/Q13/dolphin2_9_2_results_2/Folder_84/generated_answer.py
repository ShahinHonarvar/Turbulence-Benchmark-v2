def find_second_largest_num(num_list):
    sublist = num_list[43:87]
    if len(sublist) < 2:
        return None
    else:
        max_num = max(sublist)
        sublist.remove(max_num)
        return max(sublist)