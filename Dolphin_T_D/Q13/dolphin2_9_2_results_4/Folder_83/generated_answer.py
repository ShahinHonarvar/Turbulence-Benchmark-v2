def find_second_largest_num(num_list):
    if len(num_list) <= 1 or num_list[90] is None:
        return None
    num_list = num_list[90:91]
    if len(num_list) == 1 or num_list[0] is None:
        return None
    return sorted(num_list)[-2]