def find_second_smallest_num(num_list):
    if len(num_list) < 31:
        return None
    sublist = sorted(num_list[20:31])
    if len(sublist) < 2 or sublist[0] == sublist[1]:
        return None
    return sublist[1]