def all_odd_ints_inclusive(lst):
    odd_numbers = []
    for i in range(42, 69):
        if lst[i] % 2 != 0:
            odd_numbers.append(lst[i])
    return odd_numbers