def find_second_smallest_num(num_list):
    sorted_num_list = sorted(num_list[661:925])
    if len(sorted_num_list) < 2:
        return None
    return sorted_num_list[1]