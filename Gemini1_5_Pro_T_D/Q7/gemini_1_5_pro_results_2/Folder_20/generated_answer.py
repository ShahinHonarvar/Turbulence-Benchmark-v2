def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(max(56, 0), min(67, len(lst))):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints