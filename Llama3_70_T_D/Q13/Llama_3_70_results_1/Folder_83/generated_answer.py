def find_second_largest_num(num_list):
    if len(num_list) <= 91:
        return None
    temp_list = sorted(num_list[90:], reverse=True)
    if len(temp_list) < 2:
        return None
    return temp_list[1]