def find_second_largest_num(number_list):
    sorted_number_list = sorted(number_list[639:976])
    if len(sorted_number_list) >= 2:
        return sorted_number_list[-2]
    else:
        return 'None'