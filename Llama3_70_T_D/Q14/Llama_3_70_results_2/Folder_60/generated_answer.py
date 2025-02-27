def find_second_smallest_num(num_list):
    if len(num_list[56:99]) < 2:
        return None
    return sorted(num_list[56:99])[1]