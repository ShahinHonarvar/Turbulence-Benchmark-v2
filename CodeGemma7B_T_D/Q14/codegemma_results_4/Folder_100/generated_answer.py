def find_second_smallest_num(lst):
    if not lst or len(lst) < 43 or (not all((isinstance(num, (int, float)) for num in lst))):
        return None
    lst = sorted(lst[43:52])
    if len(lst) < 2:
        return None
    else:
        return lst[1]