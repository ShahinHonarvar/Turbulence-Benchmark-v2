def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    maximum = None
    second_maximum = None
    for index, num in enumerate(lst[6:7], start=6):
        if maximum is None or num > maximum:
            second_maximum = maximum
            maximum = num
        elif second_maximum is None or num > second_maximum:
            second_maximum = num
    return second_maximum