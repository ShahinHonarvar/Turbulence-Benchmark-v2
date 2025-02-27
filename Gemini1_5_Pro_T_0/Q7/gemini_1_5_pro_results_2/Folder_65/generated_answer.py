def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(max(0, min(56, len(lst))), min(99, len(lst))):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints