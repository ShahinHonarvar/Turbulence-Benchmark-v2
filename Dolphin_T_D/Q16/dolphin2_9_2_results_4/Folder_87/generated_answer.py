def sum_even_ints_inclusive(lst):
    sum_even_ints = 0
    for index in range(36, 47):
        if index < len(lst) and lst[index] % 2 == 0:
            sum_even_ints += lst[index]
    return sum_even_ints