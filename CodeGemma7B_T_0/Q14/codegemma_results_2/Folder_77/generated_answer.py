def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 639 or len(num_list) > 975:
        return 'None'
    num_list = sorted(num_list[639:976])
    return num_list[1]