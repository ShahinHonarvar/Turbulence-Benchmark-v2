def find_second_largest_num(lst):
    if len(lst) < 202 or len(lst) > 10000 or (not all((isinstance(num, int) for num in lst))):
        return None
    lst.sort()
    if 30 < len(lst) <= 200:
        return lst[-2]
    else:
        return None