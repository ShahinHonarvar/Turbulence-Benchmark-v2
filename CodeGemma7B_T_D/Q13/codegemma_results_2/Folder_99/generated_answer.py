def find_second_largest_num(num_list):
    if len(num_list) >= 1:
        num_list.sort(reverse=True)
        if len(num_list) > 310:
            return num_list[310]
    return 'None'