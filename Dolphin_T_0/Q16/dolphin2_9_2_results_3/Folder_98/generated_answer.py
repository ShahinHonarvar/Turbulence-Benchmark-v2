def sum_even_ints_inclusive(l: list[int]) -> int:
    total = 0
    for i in range(7):
        if l[i] % 2 == 0:
            total += l[i]
    return total