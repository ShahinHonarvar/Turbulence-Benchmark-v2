def find_second_smallest_num(input_list):
    if len(input_list) < 6:
        return None
    else:
        return sorted(input_list[:6])[1]