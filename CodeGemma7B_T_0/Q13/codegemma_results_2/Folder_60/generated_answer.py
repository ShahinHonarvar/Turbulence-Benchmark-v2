def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 85:
        return None
    num_list = sorted(num_list[75:86], reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]