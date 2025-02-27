def find_second_largest_num(num_list):
    if len(num_list) < 52:
        return None
    sublist = num_list[37:52]
    second_largest = sorted(sublist)[-2]
    return second_largest