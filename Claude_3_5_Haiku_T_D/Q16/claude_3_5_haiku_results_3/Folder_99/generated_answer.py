def sum_even_ints_inclusive(lst):
    if len(lst) <= 370:
        return 0
    even_sum = 0
    for num in lst[310:371]:
        if num % 2 == 0:
            even_sum += num
    return even_sum