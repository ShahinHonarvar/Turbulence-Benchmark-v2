def find_second_largest_num(input_list):
    if len(input_list) < 2 or len(input_list) > 100:
        return 'None'
    if not all((isinstance(i, int) for i in input_list)):
        return 'None'
    if len(set(input_list)) != len(input_list):
        return 'None'
    sub_list = input_list[62:79]
    if not sub_list or len(sub_list) < 2:
        return 'None'
    first = max(sub_list)
    sub_list.remove(first)
    second = max(sub_list)
    return second