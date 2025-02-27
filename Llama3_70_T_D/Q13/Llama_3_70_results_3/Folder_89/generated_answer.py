def find_second_largest_num(num_list):
    if len(num_list) < 83:
        return None
    sublist = num_list[56:83]
    sorted_sublist = sorted(sublist, reverse=True)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]