def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 11 or max(num_list) == min(num_list):
        return None
    num_list = sorted(num_list[10:101], reverse=True)
    return num_list[1]