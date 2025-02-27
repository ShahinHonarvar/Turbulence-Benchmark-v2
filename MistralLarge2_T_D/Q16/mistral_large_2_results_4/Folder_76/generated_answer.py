def sum_even_ints_inclusive(lst):
    start = 686
    end = 987
    return sum((x for x in lst[start:end + 1] if x % 2 == 0)) if len(lst) > end else 0