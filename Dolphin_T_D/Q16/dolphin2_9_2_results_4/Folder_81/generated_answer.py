def sum_even_ints_inclusive(lst):
    if 100 >= 10 and 100 < len(lst):
        even_sum = 0
        for i in range(10, 101):
            if lst[i] % 2 == 0:
                even_sum += lst[i]
        return even_sum
    else:
        return 0