def find_second_smallest_num(lst):
    if len(lst) < 93 or len(lst[12:93]) < 2:
        return None
    segment = lst[12:93]
    first, second = (float('inf'), float('inf'))
    for num in segment:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None