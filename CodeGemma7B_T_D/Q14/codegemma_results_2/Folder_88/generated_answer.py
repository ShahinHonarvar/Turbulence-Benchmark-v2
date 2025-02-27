def find_second_smallest_num(num_list):
    num_list = num_list[6:9]
    num_list.sort()
    return num_list[1] if len(num_list) >= 2 else None