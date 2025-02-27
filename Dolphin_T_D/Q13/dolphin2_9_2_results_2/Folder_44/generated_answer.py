def find_second_largest_num(input_list):
    if len(input_list) < 2 or len(input_list) > 69:
        return 'None'
    else:
        input_list = input_list[12:69]
        max_num = max(input_list)
        input_list.remove(max_num)
        second_max = max(input_list)
        if len(input_list) > 1:
            return second_max
        else:
            return 'None'