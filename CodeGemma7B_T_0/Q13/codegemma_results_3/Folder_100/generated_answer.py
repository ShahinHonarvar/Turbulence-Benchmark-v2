def find_second_largest_num(num_list):
    if len(num_list) < 43 or len(num_list) > 69:
        return None
    num_list.sort(reverse=True)
    return num_list[42:69][1]