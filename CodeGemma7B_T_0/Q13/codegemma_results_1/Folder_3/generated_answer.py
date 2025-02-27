def find_second_largest_num(num_list):
    if len(num_list) < 95 or not (62 <= min(num_list) and max(num_list) <= 92):
        return None
    num_list = sorted(num_list[62:93], reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]