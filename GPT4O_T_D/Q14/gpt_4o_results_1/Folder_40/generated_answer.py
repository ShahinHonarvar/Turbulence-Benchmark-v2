def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    sublist = lst[0:3]
    first, second = (float('inf'), float('inf'))
    for num in sublist:
        if num < first:
            second = first
            first = num
        elif num < second:
            second = num
    return second if second != float('inf') else None