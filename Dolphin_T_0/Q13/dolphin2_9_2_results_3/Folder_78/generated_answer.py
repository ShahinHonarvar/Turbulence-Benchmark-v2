def find_second_largest_num(lst):
    sublist = lst[43:52]
    if len(sublist) < 2:
        return None
    largest = max(sublist)
    second_largest = None
    for number in sublist:
        if number != largest and (second_largest is None or number > second_largest):
            second_largest = number
    return second_largest