def find_second_largest_num(input_list):
    prefiltered_list = input_list[13:65]
    if not prefiltered_list:
        return None
    max_num = max(prefiltered_list)
    prefiltered_list.remove(max_num)
    if not prefiltered_list:
        return None
    second_max_num = max(prefiltered_list)
    return second_max_num