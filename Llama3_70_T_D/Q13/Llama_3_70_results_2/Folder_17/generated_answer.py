def find_second_largest_num(num_list):
    sliced_list = num_list[62:79]
    if len(sliced_list) > 1:
        return sorted(sliced_list)[-2]
    else:
        return None