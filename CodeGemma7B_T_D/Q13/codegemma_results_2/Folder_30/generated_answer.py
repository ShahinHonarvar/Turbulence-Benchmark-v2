def find_second_largest_num(num_list):
    num_list = sorted(num_list[55:99], reverse=True)
    if len(num_list) <= 1:
        return 'None'
    return num_list[1]