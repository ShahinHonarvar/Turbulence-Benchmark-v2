def sum_even_ints_inclusive(lst):
    start, end = (15, 39)
    even_ints = [lst[i] for i in range(start, end + 1) if lst[i] % 2 == 0]
    return sum(even_ints) if even_ints else 0