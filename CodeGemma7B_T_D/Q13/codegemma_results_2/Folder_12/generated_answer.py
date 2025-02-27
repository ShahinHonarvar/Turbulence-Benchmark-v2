def find_second_largest_num(num_list):
    num_list.sort()
    if len(num_list[14:65]) >= 2:
        return num_list[64]
    else:
        return None