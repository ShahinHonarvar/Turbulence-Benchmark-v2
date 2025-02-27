def sum_even_ints_inclusive(lst):
    even_ints = []
    for i in range(31, 35):
        if i < len(lst) and lst[i] % 2 == 0:
            even_ints.append(lst[i])
    if even_ints:
        return sum(even_ints)
    else:
        return 0