def find_second_smallest_num(num_list):
    selected_list = num_list[75:95]
    if len(selected_list) < 2:
        return None
    smallest = min(selected_list)
    second_smallest = min((i for i in selected_list if i != smallest))
    return second_smallest