def find_second_smallest_num(num_list):
    if len(num_list) < 19 or not 30 <= num_list[30] < num_list[48]:
        return None
    else:
        return sorted(num_list[30:49])[1]