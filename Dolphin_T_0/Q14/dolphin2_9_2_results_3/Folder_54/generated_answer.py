def find_second_smallest_num(input_list):
    if 86 < len(input_list):
        sub_list = input_list[68:87]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
    return None