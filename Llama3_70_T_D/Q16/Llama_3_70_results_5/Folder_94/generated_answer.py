def sum_even_ints_inclusive(lst):
    start = 28
    end = 40
    total = sum((i for i in lst[start:end + 1] if i % 2 == 0))
    return total