def sum_even_ints_inclusive(lst):
    if not lst:
        return 0
    try:
        return sum((lst[i] for i in range(209, 567) if lst[i] % 2 == 0))
    except:
        return 0