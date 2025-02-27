def find_second_smallest_num(num_list):
    num_list = sorted(num_list)
    if 56 <= len(num_list) <= 98:
        return num_list[57]
    else:
        return None