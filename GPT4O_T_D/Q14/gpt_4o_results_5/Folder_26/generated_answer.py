def find_second_smallest_num(lst):
    if len(lst) < 79:
        return None
    sub_list = lst[62:79]
    if len(sub_list) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first_min:
            second_min = first_min
            first_min = number
        elif first_min < number < second_min:
            second_min = number
    return second_min if second_min != float('inf') else None