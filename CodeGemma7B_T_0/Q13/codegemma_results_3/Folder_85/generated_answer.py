def find_second_largest_num(num_list):
    if len(num_list) < 9 or num_list[6] == num_list[8]:
        return None
    return sorted(num_list[6:9])[-2]