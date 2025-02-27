def find_second_largest_num(input_list):
    subset_list = input_list[28:40]
    if len(subset_list) < 2:
        return None
    first_max = max(subset_list)
    subset_list.remove(first_max)
    second_max = max(subset_list)
    return second_max