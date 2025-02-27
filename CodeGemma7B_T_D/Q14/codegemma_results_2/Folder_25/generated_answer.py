def find_second_smallest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list) > 36 and len(num_list) < 77:
        return num_list[37]
    else:
        return None