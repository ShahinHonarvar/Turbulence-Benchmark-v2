def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) >= 87 - 30 + 1:
        return num_list[30]
    else:
        return None