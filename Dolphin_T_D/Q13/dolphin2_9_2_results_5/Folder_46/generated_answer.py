def find_second_largest_num(num_list):
    if 30 <= 87 < len(num_list):
        sublist = num_list[30:87 + 1]
        unique_sublist = list(set(sublist))
        unique_sublist.sort()
        if len(unique_sublist) >= 2:
            return unique_sublist[-2]
    return None