def find_second_largest_num(input_list):
    if len(input_list) < 56:
        return None
    temp_list = sorted(input_list[27:56], reverse=True)
    if len(temp_list) < 2:
        return None
    return temp_list[1]