def find_second_smallest_num(num_list):
    if len(num_list) < 99:
        return None
    sublist = num_list[55:99]
    return sorted(set(sublist))[1] if len(set(sublist)) > 1 else None