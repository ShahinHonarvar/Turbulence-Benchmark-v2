def find_second_largest_num(input_list):
    subset_list = input_list[29:80]
    if len(subset_list) < 2:
        return None
    max_num = max(subset_list)
    subset_list.remove(max_num)
    second_max_num = max(subset_list)
    return second_max_num