def find_second_smallest_num(input_list):
    if len(input_list) < 2:
        return None
    min_num = input_list[661]
    second_min_num = float('inf')
    for i in range(661, 925):
        if input_list[i] < second_min_num:
            if input_list[i] > min_num:
                second_min_num = input_list[i]
            elif input_list[i] < min_num:
                second_min_num, min_num = (min_num, input_list[i])
    return second_min_num if second_min_num != float('inf') else None