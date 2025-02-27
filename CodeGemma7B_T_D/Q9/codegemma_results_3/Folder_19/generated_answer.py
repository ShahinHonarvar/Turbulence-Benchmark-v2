def all_odd_ints_inclusive(lst):
    result = [lst[i] for i in range(3, 6) if lst[i] % 2 == 1]
    return result if result else []