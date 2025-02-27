def find_second_smallest_num(num_list):
    if len(num_list) < 2 or num_list[8] == num_list[9]:
        return None
    else:
        return sorted(num_list[8:10])[1]