def find_second_smallest_num(num_list):
    if not num_list:
        return None
    sub_list = num_list[37:77]
    if len(sub_list) < 2:
        return None
    min_value, second_min_value = (sub_list[0], float('inf'))
    for num in sub_list:
        if num < min_value:
            min_value, second_min_value = (num, min_value)
        elif min_value < num < second_min_value:
            second_min_value = num
    return second_min_value if second_min_value != float('inf') else None