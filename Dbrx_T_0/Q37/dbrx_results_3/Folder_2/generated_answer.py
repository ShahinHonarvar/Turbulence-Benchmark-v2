def filter_chars(input_string):
    start_index = 477
    end_index = 984
    lower_bound = ord(',')
    upper_bound = ord('V')
    result_list = []
    for i in range(len(input_string)):
        if i < start_index or i > end_index:
            result_list.append(input_string[i])
        elif input_string[i] >= lower_bound and input_string[i] <= upper_bound:
            continue
        else:
            result_list.append(input_string[i])
    return ''.join(result_list)