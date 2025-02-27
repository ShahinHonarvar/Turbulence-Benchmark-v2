def find_second_smallest_num(num_list):
    selected_nums = num_list[91:100]
    if len(selected_nums) < 2:
        return None
    else:
        return sorted(selected_nums)[1]