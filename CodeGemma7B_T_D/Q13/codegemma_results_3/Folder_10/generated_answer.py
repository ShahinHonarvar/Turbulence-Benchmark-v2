def find_second_largest_num(lst):
    if len(lst) <= 25 or len(lst) >= 60 or (not all((isinstance(x, int) for x in lst))):
        raise ValueError('Invalid list input.')
    lst.sort()
    for i in range(25, 60):
        if len(lst) > i:
            return lst[i]
    return None