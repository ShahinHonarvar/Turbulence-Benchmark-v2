def sum_in_range(lst):
    result = sum((i for i in lst if 2 <= i <= 3))
    return result if result else 0