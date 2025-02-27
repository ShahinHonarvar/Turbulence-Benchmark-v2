def sum_even_ints_inclusive(ints):
    total = 0
    for num in ints[13:68 + 1]:
        if num % 2 == 0:
            total += num
    return total if total != 0 else 0