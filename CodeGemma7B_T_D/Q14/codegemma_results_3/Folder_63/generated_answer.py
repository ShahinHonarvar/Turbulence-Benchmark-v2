def find_second_smallest_num(lst):
    if len(lst) < 57 or len(lst) > 83:
        return 'None'
    lst.sort(reverse=True)
    return lst[56:83]