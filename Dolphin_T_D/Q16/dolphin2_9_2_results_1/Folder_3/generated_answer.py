def sum_even_ints_inclusive(numbers):
    total = 0
    for i in range(62, 93):
        if numbers[i] % 2 == 0:
            total += numbers[i]
    return total if total != 0 else 0