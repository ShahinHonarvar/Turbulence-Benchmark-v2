def find_second_smallest_num(num_list):
    if len(num_list) < 47 or num_list[36] is None:
        return 'None'
    temp_list = sorted(num_list[36:47])
    return temp_list[1] if len(temp_list) > 1 else 'None'