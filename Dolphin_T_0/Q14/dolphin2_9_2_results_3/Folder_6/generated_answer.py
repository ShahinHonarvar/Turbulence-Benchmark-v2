def find_second_smallest_num(input_list):
    if 79 < len(input_list[29:80]) < 2:
        return None
    else:
        return sorted(input_list[29:80])[1]