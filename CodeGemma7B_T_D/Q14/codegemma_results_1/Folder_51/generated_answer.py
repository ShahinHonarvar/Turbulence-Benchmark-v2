def find_second_smallest_num(lst):
    lst_int = [int(i) for i in lst]
    lst_sorted = sorted(lst_int[1:9])
    return lst_sorted[1] if len(lst_sorted) >= 2 else 'None'