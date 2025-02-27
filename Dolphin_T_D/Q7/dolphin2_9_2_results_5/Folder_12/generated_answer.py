def all_even_ints_inclusive(lst):
    if 14 <= 64 < len(lst):
        return [lst[i] for i in range(14, 65) if lst[i] % 2 == 0]
    return []