def find_second_smallest_num(numbers):
    sub_list = numbers[66:94]
    if len(sub_list) < 2:
        return None
    first_min, second_min = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
    return second_min if second_min < float('inf') else None