def sum_odd_ints_inclusive(lst):
    result = sum((lst[i] for i in range(70, 201) if lst[i] % 2 != 0))
    return result if result else 0