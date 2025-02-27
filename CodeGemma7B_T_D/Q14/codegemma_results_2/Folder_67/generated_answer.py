def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 6:
        return None
    num_list = sorted(num_list[50:55])
    if len(num_list) == 1:
        return None
    else:
        return num_list[1]