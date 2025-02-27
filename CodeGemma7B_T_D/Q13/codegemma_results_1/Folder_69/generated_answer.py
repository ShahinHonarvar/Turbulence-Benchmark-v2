def find_second_largest_num(num_list):
    if len(num_list) <= 35 or num_list[32] is None or num_list[35] is None:
        return None
    num_list.sort()
    return num_list[35]