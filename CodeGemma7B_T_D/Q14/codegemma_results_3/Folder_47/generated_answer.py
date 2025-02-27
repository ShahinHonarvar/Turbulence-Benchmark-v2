def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) < 25:
        return None
    else:
        return num_list[22]

def find_min_max_dif(num_list):
    if not num_list:
        return None
    else:
        return max(num_list) - min(num_list)