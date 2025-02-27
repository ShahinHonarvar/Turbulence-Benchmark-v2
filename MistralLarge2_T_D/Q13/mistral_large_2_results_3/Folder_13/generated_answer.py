def find_second_largest_num(num_list):
    sorted_list = sorted(num_list[25:88], reverse=True)
    return sorted_list[1] if len(sorted_list) > 1 else None