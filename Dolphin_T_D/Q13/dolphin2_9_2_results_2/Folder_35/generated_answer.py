def find_second_largest_num(input_list):
    if len(input_list) < 49:
        return None
    sublist = input_list[30:49]
    if len(set(sublist)) < 2:
        return None
    return sorted(sublist)[-2]