def find_second_smallest_num(num_list):
    selected_list = num_list[2:6]
    if len(set(selected_list)) < 2:
        return None
    else:
        selected_list.sort()
        return selected_list[1]