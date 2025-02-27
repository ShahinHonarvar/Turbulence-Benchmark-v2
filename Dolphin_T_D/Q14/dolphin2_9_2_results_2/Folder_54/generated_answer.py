def find_second_smallest_num(input_list):
    if not input_list:
        return None
    sublist = input_list[68:87]
    if len(sublist) < 2:
        return None
    second_smallest = min(sublist[1:], default=None)
    return second_smallest