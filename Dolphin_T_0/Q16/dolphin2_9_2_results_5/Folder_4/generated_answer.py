def sum_even_ints_inclusive(lst):
    result = 0
    for i in range(12, 93):
        if i < len(lst):
            if lst[i] % 2 == 0:
                result += lst[i]
    return result