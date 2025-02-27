def sum_in_range(lst):
    result = sum((i for i in lst if 20 <= i <= 93))
    if result:
        return result
    else:
        return 0