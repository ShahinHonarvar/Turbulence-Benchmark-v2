def find_second_smallest_num(num_list):
    if len(num_list) > 63:
        num_list = sorted(num_list[62:64])
        if len(num_list) > 1:
            return num_list[1]
    return None