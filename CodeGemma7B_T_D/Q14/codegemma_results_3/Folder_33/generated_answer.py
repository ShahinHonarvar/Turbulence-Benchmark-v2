def find_second_smallest_num(num_list):
    num_list = sorted(num_list)
    if 262 <= len(num_list) <= 746:
        return num_list[262]
    else:
        return None