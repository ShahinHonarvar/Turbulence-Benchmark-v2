def find_second_smallest_num(num_list):
    if 91 <= len(num_list) <= 99:
        num_list.sort()
        return num_list[91]
    else:
        return None