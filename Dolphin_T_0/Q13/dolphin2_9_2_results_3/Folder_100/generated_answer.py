def find_second_largest_num(input_list):
    if len(input_list) == 0 or len(input_list) < 2:
        return None
    else:
        input_list = input_list[41:69]
        input_list.sort(reverse=True)
        return input_list[1]