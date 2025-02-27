def find_second_largest_num(num_list):
    if len(num_list) < 52 or not (43 <= min(num_list) and max(num_list) <= 51):
        return None
    num_list = sorted(num_list[43:52], reverse=True)
    if len(num_list) < 2:
        return None
    return num_list[1]