def sum_odd_ints_inclusive(lst):
    total = 0
    for index in range(35, 50):
        if index < len(lst) and lst[index] % 2 != 0:
            total += lst[index]
    return total