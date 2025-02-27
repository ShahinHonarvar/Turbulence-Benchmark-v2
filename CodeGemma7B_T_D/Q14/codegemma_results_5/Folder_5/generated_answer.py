def find_second_smallest_num(num_list):
    length = len(num_list)
    if length < 5:
        return None
    num_list.sort()
    return num_list[3]