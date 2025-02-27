def find_second_smallest_num(num_list):
    if 25 <= len(num_list) <= 59:
        sorted_sublist = sorted(num_list[25:60])
        return sorted_sublist[1] if len(sorted_sublist) > 1 else None
    return None