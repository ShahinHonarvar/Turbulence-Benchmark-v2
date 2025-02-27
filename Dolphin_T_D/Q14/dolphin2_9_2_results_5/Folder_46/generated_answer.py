def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    sublist = lst[13:69]
    if len(sublist) < 2:
        return None
    smallest = sublist[0]
    second_smallest = None
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif second_smallest is None or (num < second_smallest and num > smallest):
            second_smallest = num
    return second_smallest