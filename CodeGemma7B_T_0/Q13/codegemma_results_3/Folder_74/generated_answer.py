def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 17 or len(num_list) > 78:
        return None
    num_list = sorted(num_list[17:79], reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]