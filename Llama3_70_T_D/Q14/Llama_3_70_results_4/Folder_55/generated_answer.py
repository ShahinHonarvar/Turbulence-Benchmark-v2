def find_second_smallest_num(num_list):
    if len(num_list) <= 10:
        return None
    else:
        return sorted(num_list[10:11])[1] if len(set(num_list[10:11])) > 1 else None