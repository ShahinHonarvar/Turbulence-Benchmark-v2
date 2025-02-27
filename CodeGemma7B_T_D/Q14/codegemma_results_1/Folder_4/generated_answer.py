def find_second_smallest_num(num_list):
    if len(num_list) is 0 or len(num_list) is 1:
        return None
    sorted_num_list = sorted(num_list)
    for item in sorted_num_list[70:85]:
        return item
    return None