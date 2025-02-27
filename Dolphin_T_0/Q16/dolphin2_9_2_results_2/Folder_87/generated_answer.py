def sum_even_ints_inclusive(lst):
    summation = 0
    for num in lst[36:47]:
        if num % 2 == 0:
            summation += num
    return summation if summation != 0 else 0