def find_second_largest_num(lst):
    if len(lst) < 2 or len(lst) > 78:
        return None
    first = max(lst[17:79])
    second = None
    for i in lst[17:79]:
        if i != first and (second is None or i > second):
            second = i
    return second