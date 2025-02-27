def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    sub_list = lst[0:3]
    first, second = (float('inf'), float('inf'))
    for number in sub_list:
        if number < first:
            first, second = (number, first)
        elif first < number < second:
            second = number
    return second if second != float('inf') else None