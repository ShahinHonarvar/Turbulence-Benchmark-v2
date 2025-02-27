def all_even_ints_inclusive(lst):
    try:
        return [lst[i] for i in range(82, 87) if lst[i] % 2 == 0]
    except IndexError:
        return []