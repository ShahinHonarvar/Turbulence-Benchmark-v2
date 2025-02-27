def sum_odd_ints_inclusive(l: list) -> int:
    sum_them = sum((val for i, val in enumerate(l[50:201]) if i % 2 != 0))
    return sum_them if sum_them != 0 else 0