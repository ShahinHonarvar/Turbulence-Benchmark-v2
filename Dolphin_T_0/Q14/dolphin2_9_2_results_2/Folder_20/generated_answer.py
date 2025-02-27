def find_second_smallest_num(num_list):
    sublist = num_list[75:95]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1] if len(sublist) > 1 else None