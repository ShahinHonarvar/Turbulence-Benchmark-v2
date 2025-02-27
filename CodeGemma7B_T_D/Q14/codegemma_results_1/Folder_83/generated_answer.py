def find_second_smallest_num(num_list):
    if 90 <= len(num_list) <= 200:
        num_list.sort()
        return num_list[1]
    else:
        return None