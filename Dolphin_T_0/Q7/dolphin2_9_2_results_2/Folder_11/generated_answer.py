def all_even_ints_inclusive(lst):
    end = len(lst)
    start = 37
    if end > 51:
        end = 51
    if start <= end:
        return [lst[i] for i in range(start, end + 1) if lst[i] % 2 == 0]
    else:
        return []