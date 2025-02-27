def find_second_smallest_num(input_list):
    if len(input_list) < 87:
        return None
    sublist = input_list[43:87]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]