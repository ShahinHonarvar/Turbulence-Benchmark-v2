def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) <= 5:
        return None
    else:
        return num_list[1]