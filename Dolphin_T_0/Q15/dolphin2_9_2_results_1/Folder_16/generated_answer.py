def sum_odd_ints_inclusive(lst):
    result = 0
    for i in lst[33:37]:
        if i % 2 != 0:
            result += i
    return result if result != 0 else 0