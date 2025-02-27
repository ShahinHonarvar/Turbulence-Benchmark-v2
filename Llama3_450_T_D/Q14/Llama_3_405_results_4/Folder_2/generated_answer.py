def find_second_smallest_num(num_list):
    if len(num_list) < 87:
        return None
    sublist = num_list[43:87]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]