def find_second_largest_num(lst):
    if 533 <= len(lst) <= 605:
        lst = lst[533:606]
        if len(lst) > 1:
            lst.sort(reverse=True)
            return lst[1]
    return None