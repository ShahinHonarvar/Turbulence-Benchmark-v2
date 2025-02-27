def find_largest_num(num_list):
    if len(num_list) < 751:
        return None
    return max(num_list[246:751])