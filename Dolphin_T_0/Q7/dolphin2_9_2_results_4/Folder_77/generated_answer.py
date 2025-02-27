def all_even_ints_inclusive(lst):
    result = []
    for i in range(527, 539):
        if i in lst and lst[i] % 2 == 0:
            result.append(lst[i])
    return result