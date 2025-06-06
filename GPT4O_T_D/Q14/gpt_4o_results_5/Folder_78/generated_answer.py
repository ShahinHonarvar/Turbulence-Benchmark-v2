def find_second_smallest_num(lst):
    if len(lst) < 78:
        return None
    sub_list = lst[17:79]
    if len(sub_list) < 2:
        return None
    first = float('inf')
    second = float('inf')
    for num in sub_list:
        if num < first:
            second = first
            first = num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None