def find_second_largest_num(input_list):
    if not input_list:
        return None
    sublist = input_list[22:51]
    if len(sublist) == 1:
        return None
    sorted_sublist = sorted(set(sublist))
    return sorted_sublist[-2] if len(sorted_sublist) > 1 else None