def find_second_smallest_num(num_list):
    if len(num_list[36:47]) >= 2:
        num_list[36:47].sort()
        return num_list[37]
    else:
        return None