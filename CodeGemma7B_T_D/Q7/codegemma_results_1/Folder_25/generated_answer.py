def all_even_ints_inclusive(lst):
    filtered_lst = []
    for k in range(29, 94):
        if lst[k] % 2 == 0:
            filtered_lst.append(lst[k])
    return filtered_lst