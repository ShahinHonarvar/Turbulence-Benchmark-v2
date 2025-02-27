def find_second_smallest_num(num_list):
    if len(num_list) < 82 or 82 not in range(len(num_list)):
        return None
    num_list.sort()
    return num_list[56:83][1]