def find_second_smallest_num(num_list):
    if len(num_list) < 87:
        return None
    sublist = sorted(num_list[68:87])
    if len(sublist) < 2:
        return None
    return sublist[1]