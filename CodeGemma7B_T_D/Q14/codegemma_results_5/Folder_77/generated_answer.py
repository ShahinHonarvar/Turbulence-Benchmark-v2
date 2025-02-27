def find_second_smallest_num(num_list):
    num_list = sorted(num_list[639:976])
    if len(num_list) >= 2:
        return num_list[1]
    else:
        return None