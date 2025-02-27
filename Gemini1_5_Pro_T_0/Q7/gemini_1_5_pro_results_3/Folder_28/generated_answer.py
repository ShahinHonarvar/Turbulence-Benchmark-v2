def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(max(0, min(62, len(lst))), min(64, len(lst))):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints