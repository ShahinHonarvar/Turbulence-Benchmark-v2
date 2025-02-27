def sum_even_ints_inclusive(lst):
    if len(lst) <= 29:
        return 0
    else:
        even_sum = 0
        for num in lst[29:30]:
            if num % 2 == 0:
                even_sum += num
        return even_sum