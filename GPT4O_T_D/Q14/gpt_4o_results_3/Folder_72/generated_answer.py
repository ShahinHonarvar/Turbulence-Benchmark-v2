def find_second_smallest_num(lst):
    if len(lst) < 87:
        return None
    sub_list = lst[82:87]
    if len(sub_list) < 2:
        return None
    first = second = float('inf')
    for number in sub_list:
        if number < first:
            second = first
            first = number
        elif first < number < second:
            second = number
    return second if second != float('inf') else None