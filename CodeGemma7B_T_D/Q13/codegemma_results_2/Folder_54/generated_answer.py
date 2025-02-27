def find_second_largest_num(num_list):
    if not 34 <= len(num_list) <= 55:
        return None
    num_list.sort(reverse=True)
    if len(num_list) <= 1:
        return None
    return num_list[1]