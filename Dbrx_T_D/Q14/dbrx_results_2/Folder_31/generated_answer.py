def find_second_smallest_num(input_list):
    if len(input_list) < 2:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in input_list[29:94]:
        if num <= min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num and num > min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None