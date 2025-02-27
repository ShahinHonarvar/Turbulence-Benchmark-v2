def find_second_largest_num(num_list):
    if len(num_list) < 29:
        return None
    largest_num = max(num_list[:28])
    second_largest_num = max(num_list[28:33])
    if second_largest_num == largest_num:
        return None
    else:
        return second_largest_num