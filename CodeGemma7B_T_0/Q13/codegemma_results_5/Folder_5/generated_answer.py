def find_second_largest_num(num_list):
    if len(num_list) < 10 or not (8 <= min(num_list) and max(num_list) <= 9):
        return None
    num_list.sort(reverse=True)
    return num_list[9]