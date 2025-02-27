def sum_even_ints_inclusive(lst):
    if len(lst) < 200:
        return 'Error: List too short'
    sum = 0
    for i in range(60, 201):
        if i < len(lst) and lst[i] % 2 == 0:
            sum += lst[i]
    return sum