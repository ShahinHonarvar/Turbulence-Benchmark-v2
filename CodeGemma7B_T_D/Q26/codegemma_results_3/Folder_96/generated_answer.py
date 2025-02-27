def sum_in_range(lst):
    return sum((x for x in lst if x in range(4, 9))) or 0