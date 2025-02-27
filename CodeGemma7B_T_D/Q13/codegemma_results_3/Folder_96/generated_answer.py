def find_second_largest_num(num_list):
    if not num_list:
        return None
    num_list.sort(reverse=True)
    if len(num_list) <= 15 or len(num_list) < 52:
        return None
    return num_list[14]