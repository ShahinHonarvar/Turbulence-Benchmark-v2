def find_second_largest_num(num_list):
    if len(num_list[59:98]) < 2:
        return None
    second_largest = sorted(set(num_list[59:98]))[-2]
    return second_largest