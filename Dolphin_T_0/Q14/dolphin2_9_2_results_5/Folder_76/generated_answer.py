def find_second_smallest_num(lst):
    if not lst:
        return None
    lst = [num for num in lst[533:606]]
    if len(lst) == 1:
        return None
    first_min, second_min = (lst[0], None)
    for num in lst:
        if num < first_min:
            first_min, second_min = (num, first_min)
        elif num < second_min and num != first_min:
            second_min = num
    return second_min