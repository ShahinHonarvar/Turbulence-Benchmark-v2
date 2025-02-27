def find_second_largest_num(input_list):
    if 62 <= len(input_list) <= 63:
        input_list.sort(reverse=True)
        if len(input_list) > 1:
            return input_list[1]
    return None