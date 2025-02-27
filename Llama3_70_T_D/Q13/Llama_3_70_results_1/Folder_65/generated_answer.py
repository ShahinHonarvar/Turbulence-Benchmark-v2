def find_second_largest_num(num_list):
    if len(num_list[56:99]) < 2:
        return None
    else:
        temp_list = sorted(num_list[56:99])
        return temp_list[-2]