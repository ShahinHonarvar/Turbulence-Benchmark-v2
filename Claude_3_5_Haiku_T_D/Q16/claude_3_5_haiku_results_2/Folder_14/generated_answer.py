def sum_even_ints_inclusive(lst):
    if len(lst) < 8:
        return 0
    even_sum = 0
    for num in lst[5:8]:
        if num % 2 == 0:
            even_sum += num
    return even_sum