def find_second_largest_num(input_list):
    if len(input_list) < 19:
        return None
    else:
        sublist = input_list[67:87]
        unique_values = list(set(sublist))
        unique_values.sort()
        if len(unique_values) < 2:
            return None
        else:
            return unique_values[1]