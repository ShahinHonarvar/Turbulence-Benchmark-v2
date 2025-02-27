def find_second_smallest_num(num_list):
    if 57 < len(num_list):
        sublist = sorted(num_list[56:58])
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None