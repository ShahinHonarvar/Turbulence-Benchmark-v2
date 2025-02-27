def find_second_smallest_num(num_list):
    if 37 <= len(num_list) <= 51 and len(set(num_list)) == len(num_list):
        num_list.sort()
        return num_list[40]
    else:
        return 'None'