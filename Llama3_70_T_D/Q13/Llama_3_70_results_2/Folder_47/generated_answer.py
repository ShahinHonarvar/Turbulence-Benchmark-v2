def find_second_largest_num(num_list):
    selected_list = num_list[37:77]
    selected_list.sort(reverse=True)
    if len(selected_list) < 2:
        return None
    return selected_list[1]