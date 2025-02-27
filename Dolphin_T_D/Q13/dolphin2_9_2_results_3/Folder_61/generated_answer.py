def find_second_largest_num(num_list):
    max_n1 = max(num_list[0:8])
    num_list.remove(max_n1)
    if len(num_list[0:8]) > 0:
        max_n2 = max(num_list[0:8])
        return max_n2
    else:
        return None