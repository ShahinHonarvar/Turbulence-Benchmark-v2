def find_second_largest_num(num_list):
    if len(num_list[56:99]) < 2:
        return None
    else:
        return sorted(set(num_list[56:99]), reverse=True)[1]