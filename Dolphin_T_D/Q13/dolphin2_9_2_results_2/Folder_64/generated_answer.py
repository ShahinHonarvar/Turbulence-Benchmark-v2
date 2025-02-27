def find_second_largest_num(input_list):
    if len(input_list) < 5:
        return None
    else:
        return sorted(input_list[:5])[3]