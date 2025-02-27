def find_second_largest_num(num_list):
    if len(num_list) < 6 or num_list[3] == num_list[4] == num_list[5]:
        return 'None'
    return sorted(num_list[3:6])[-2]