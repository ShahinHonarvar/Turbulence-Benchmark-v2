def find_second_largest_num(num_list):
    if len(num_list) < 69:
        return None
    return sorted(set(num_list[13:69]), reverse=True)[1] if len(set(num_list[13:69])) > 1 else None