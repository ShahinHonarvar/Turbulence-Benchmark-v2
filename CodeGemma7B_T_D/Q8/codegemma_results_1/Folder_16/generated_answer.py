def all_even_ints_exclusive(lst):
    even_nums_in_range = []
    for i in range(86, 90):
        if lst[i] % 2 == 0:
            even_nums_in_range.append(lst[i])
    return even_nums_in_range or []