def sum_even_ints_inclusive(numbers):
    total = 0
    for i in range(30, 201, 2):
        total += numbers[i]
    return total if total else 0