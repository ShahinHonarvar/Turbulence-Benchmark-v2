def find_second_largest_num(num_list):
    num_list.sort(reverse=True)
    if len(num_list) < 246 or len(num_list) > 751:
        return None
    return num_list[246]