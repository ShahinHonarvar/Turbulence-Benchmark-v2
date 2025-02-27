def find_second_smallest_num(lst):
    if not lst or len(lst) < 15 or (not all((isinstance(num, int) for num in lst))):
        return 'None'
    lst = lst[37:52]
    lst.sort()
    if len(lst) < 2:
        return 'None'
    return lst[1]