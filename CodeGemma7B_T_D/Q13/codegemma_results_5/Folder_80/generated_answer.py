def find_second_largest_num(number_list):
    number_list = number_list[64:67]
    if len(number_list) == 0:
        return None
    return max(number_list)