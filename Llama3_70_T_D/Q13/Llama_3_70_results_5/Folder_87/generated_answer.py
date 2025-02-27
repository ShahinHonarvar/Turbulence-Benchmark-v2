def find_second_largest_num(num_list):
    if len(num_list) < 47:
        return None
    num_list = num_list[36:47]
    return sorted(set(num_list), reverse=True)[1] if len(set(num_list)) > 1 else None