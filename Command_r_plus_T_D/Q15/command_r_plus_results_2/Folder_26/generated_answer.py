def sum_odd_ints_inclusive(lst):
    return sum(lst[62:100:1]) if all((i % 2 != 0 for i in lst[62:100:1])) else 0