def sum_even_ints_inclusive(lst_ints):
    total = 0
    for i in range(75, 89):
        if lst_ints[i] % 2 == 0:
            total += lst_ints[i]
    return total if total else 0