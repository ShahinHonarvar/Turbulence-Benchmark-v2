def find_second_largest_num(num_list):
    num_list = sorted(num_list)[6]
    if num_list == num_list[-1]:
        return None
    return num_list[-2]