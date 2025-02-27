def find_second_smallest_num(num_list):
    sublist = num_list[54:99]
    sublist.sort()
    if len(sublist) < 2:
        return None
    for i in range(1, len(sublist)):
        if sublist[i] != sublist[0]:
            return sublist[i]
    return None