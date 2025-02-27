def find_second_largest_num(num_list):
    if 50 <= len(num_list) <= 54:
        sorted_list = sorted(num_list[50:55], reverse=True)
        return sorted_list[1] if len(sorted_list) > 1 else None
    return None