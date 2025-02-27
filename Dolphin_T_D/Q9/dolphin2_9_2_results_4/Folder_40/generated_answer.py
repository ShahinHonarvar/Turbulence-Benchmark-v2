def all_odd_ints_inclusive(lst):
    output = [lst[i] for i in range(3) if lst[i] % 2 != 0]
    return output