def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    sublist = num_list[34:56]
    sublist.sort(reverse=True)
    return sublist[1] if len(sublist) > 1 else None