def find_second_smallest_num(numbers):
    sub_list = numbers[42:69]
    if len(sub_list) < 2:
        return None
    second_min = min(sub_list[1:])
    min_val = min(sub_list)
    for x in sub_list:
        if x != min_val and x < second_min:
            second_min = x
    return second_min if second_min != min_val else None