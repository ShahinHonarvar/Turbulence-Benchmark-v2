def all_even_ints_exclusive(lst):
    even_ints = []
    for i in range(598, 767):
        if lst[i] % 2 == 0 and i not in range(655, 670):
            even_ints.append(lst[i])
    if not even_ints:
        return []
    return even_ints