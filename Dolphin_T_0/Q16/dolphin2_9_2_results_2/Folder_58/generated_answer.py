def sum_even_ints_inclusive(lst):
    total = 0
    for num in lst[209:557]:
        if num % 2 == 0:
            total += num
    return total if total != 0 else 0