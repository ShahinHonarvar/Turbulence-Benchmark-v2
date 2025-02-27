def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 30 or len(num_list) > 94:
        return None
    num_list = sorted(num_list)
    return num_list[-2]