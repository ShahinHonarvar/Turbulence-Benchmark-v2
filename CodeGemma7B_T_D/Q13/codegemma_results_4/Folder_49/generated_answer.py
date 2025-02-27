def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 201:
        return None
    num_list = sorted(num_list[80:201])
    return num_list[-2] if len(num_list) > 1 else None