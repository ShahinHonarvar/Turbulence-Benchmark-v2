def sum_even_ints_inclusive(lst):
    sum_even_numbers = 0
    for i in range(43, 87):
        if lst[i] % 2 == 0:
            sum_even_numbers += lst[i]
    return sum_even_numbers if sum_even_numbers != 0 else 0