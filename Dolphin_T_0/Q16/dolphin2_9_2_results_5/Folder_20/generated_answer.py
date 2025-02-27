def sum_even_ints_inclusive(lst):
    total = 0
    for num in lst[56:67]:
        if num % 2 == 0:
            total += num
    return total if total != 0 else 0