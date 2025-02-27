def find_second_largest_num(input_list):
    if 36 <= len(input_list) <= 46:
        filtered_list = input_list[36:47]
        if len(set(filtered_list)) == len(filtered_list):
            sorted_list = sorted(filtered_list, reverse=True)
            if len(filtered_list) >= 2:
                return sorted_list[1]
    return None