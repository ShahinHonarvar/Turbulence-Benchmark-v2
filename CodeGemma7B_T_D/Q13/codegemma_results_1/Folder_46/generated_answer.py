def find_second_largest_num(num_list):
    if len(num_list) > 30:
        num_list.sort()
        return num_list[30:88][-2]
    return None