def find_second_smallest_num(num_list):
    num_list.sort()
    if 52 <= len(num_list) <= 71:
        return num_list[52]
    else:
        return None