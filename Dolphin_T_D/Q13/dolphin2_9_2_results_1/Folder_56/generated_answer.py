def find_second_largest_num(input_list):
    if len(input_list) < 2:
        return 'None'
    else:
        first_largest = max(input_list)
        input_list.remove(first_largest)
        second_largest = max(input_list)
        return second_largest