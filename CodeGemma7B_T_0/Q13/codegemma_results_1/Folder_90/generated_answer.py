def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 262 or len(num_list) > 746:
        return None
    num_list.sort(reverse=True)
    return num_list[1]