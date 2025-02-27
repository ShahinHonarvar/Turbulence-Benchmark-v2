def find_second_largest_num(lst):
    if not lst or len(lst) <= 90:
        return None
    lst = lst[90:91]
    return max(lst)