def find_second_largest_num(num_list):
    if len(num_list) < 38 or len(num_list) > 52:
        return None
    num_list = sorted(num_list[37:52], reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]