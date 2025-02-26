def sum_even_ints_inclusive(integers):
    if len(integers) < 2:
        return 0
    total = 0
    for num in integers[:2]:
        if num % 2 == 0:
            total += num
    return total