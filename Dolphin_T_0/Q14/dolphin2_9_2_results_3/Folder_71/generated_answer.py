def find_second_smallest_num(input_list):
    if len(input_list) < 51:
        return None
    sub_list = input_list[29:52]
    if len(sub_list) < 2:
        return None
    sorted_list = sorted(sub_list)
    if sorted_list[1] == sorted_list[-1]:
        return None
    return sorted_list[1]